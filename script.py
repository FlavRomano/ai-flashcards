#!/usr/bin/env python3
"""
Migrate Obsidian "Flashcards" plugin format (#card headings + answer blocks)
to Obsidian "Spaced Repetition" plugin format (multi-line cards with '?' separator),
WHILE KEEPING THE ORIGINAL HEADINGS.

Behavior:
- Frontmatter:
  - removes `cards-deck: ...` and derives a deck tag `#flashcards/...` (converts :: to /)
  - removes `card` from YAML tags if present
- Body:
  - For each heading that ends with `#card`:
      1) keeps the heading (without `#card`)
      2) adds a spaced repetition card immediately below it:
            <question text>
            ?
            <answer block>
  - Answer block = everything until the next `#card` heading (or EOF)
- Inserts the derived deck tag once near the top of the note (after frontmatter),
  unless it already exists.

Usage:
  python migrate_flashcards_to_spaced_repetition_keep_headings.py input.md output.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple


CARD_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#card\s*$")
FRONTMATTER_DELIM_RE = re.compile(r"^\s*---\s*$")
CARDS_DECK_RE = re.compile(r"^\s*cards-deck\s*:\s*(.+?)\s*$", re.IGNORECASE)
TAGS_INLINE_LIST_RE = re.compile(r"^\s*tags\s*:\s*\[(.*)\]\s*$", re.IGNORECASE)
TAGS_BLOCK_START_RE = re.compile(r"^\s*tags\s*:\s*$", re.IGNORECASE)
TAGS_BLOCK_ITEM_RE = re.compile(r"^\s*-\s*(.+?)\s*$")


def extract_frontmatter(lines: List[str]) -> Tuple[Optional[List[str]], List[str]]:
    if not lines:
        return None, lines
    if not FRONTMATTER_DELIM_RE.match(lines[0]):
        return None, lines

    for i in range(1, len(lines)):
        if FRONTMATTER_DELIM_RE.match(lines[i]):
            return lines[: i + 1], lines[i + 1 :]
    return None, lines


def normalize_deck_to_tag(cards_deck_value: str) -> str:
    deck = cards_deck_value.strip()
    deck = deck.replace("::", "/").replace("\\", "/")
    deck = deck.strip("/")
    return f"#flashcards/{deck}" if deck else "#flashcards"


def process_frontmatter(fm_lines: List[str]) -> Tuple[List[str], Optional[str]]:
    deck_tag: Optional[str] = None
    out: List[str] = []

    if (
        len(fm_lines) >= 2
        and FRONTMATTER_DELIM_RE.match(fm_lines[0])
        and FRONTMATTER_DELIM_RE.match(fm_lines[-1])
    ):
        out.append(fm_lines[0].rstrip("\n"))
        inner = [l.rstrip("\n") for l in fm_lines[1:-1]]

        i = 0
        while i < len(inner):
            line = inner[i]

            m_deck = CARDS_DECK_RE.match(line)
            if m_deck:
                deck_tag = normalize_deck_to_tag(m_deck.group(1))
                i += 1
                continue

            m_inline = TAGS_INLINE_LIST_RE.match(line)
            if m_inline:
                raw = m_inline.group(1)
                items = [x.strip() for x in raw.split(",") if x.strip()]
                items = [t for t in items if t.lower() != "card"]
                out.append(f"tags: [{', '.join(items)}]" if items else "tags: []")
                i += 1
                continue

            if TAGS_BLOCK_START_RE.match(line):
                out.append(line)
                i += 1
                while i < len(inner) and TAGS_BLOCK_ITEM_RE.match(inner[i]):
                    m_item = TAGS_BLOCK_ITEM_RE.match(inner[i])
                    assert m_item is not None
                    tag_val = m_item.group(1).strip().strip('"').strip("'")
                    if tag_val.lower() != "card":
                        out.append(inner[i])
                    i += 1
                continue

            out.append(line)
            i += 1

        out.append(fm_lines[-1].rstrip("\n"))
        return [l + "\n" for l in out], deck_tag

    return fm_lines, deck_tag


def migrate_body_keep_headings(body_lines: List[str], deck_tag: Optional[str]) -> List[str]:
    out: List[str] = []

    # Avoid inserting if already present
    already_has_deck_tag = False
    if deck_tag:
        already_has_deck_tag = any(deck_tag.strip() == ln.strip() for ln in body_lines)

    idx = 0
    n = len(body_lines)

    # Insert deck tag after leading blanks (and before first content)
    if deck_tag and not already_has_deck_tag:
        j = 0
        while j < n and body_lines[j].strip() == "":
            out.append(body_lines[j])
            j += 1
        out.append(deck_tag + "\n\n")
        idx = j

    while idx < n:
        line = body_lines[idx].rstrip("\n")
        m = CARD_HEADING_RE.match(line)

        if not m:
            out.append(body_lines[idx])
            idx += 1
            continue

        hashes = m.group(1)               # '##', '###', etc.
        question_raw = m.group(2).strip() # heading text without '#card'
        question = re.sub(r"\s+#+\s*$", "", question_raw).strip()

        # 1) Keep the heading (minus #card)
        out.append(f"{hashes} {question}\n")

        # Collect answer block until next #card heading or EOF
        idx += 1
        answer_lines: List[str] = []
        while idx < n:
            peek = body_lines[idx].rstrip("\n")
            if CARD_HEADING_RE.match(peek):
                break
            answer_lines.append(body_lines[idx])
            idx += 1

        # Trim leading/trailing blank lines around the answer block
        while answer_lines and answer_lines[0].strip() == "":
            answer_lines.pop(0)
        while answer_lines and answer_lines[-1].strip() == "":
            answer_lines.pop()

        # 2) Add spaced repetition card below heading
        out.append("?\n")
        if answer_lines:
            out.extend(answer_lines)
            if not answer_lines[-1].endswith("\n"):
                out.append("\n")
        out.append("\n")  # blank line after each migrated card

    return out


def migrate_text(text: str) -> str:
    lines = text.splitlines(keepends=True)
    fm, body = extract_frontmatter(lines)

    deck_tag: Optional[str] = None
    out_lines: List[str] = []

    if fm is not None:
        fm_processed, deck_tag = process_frontmatter(fm)
        out_lines.extend(fm_processed)
        # ensure blank line after frontmatter
        if out_lines and out_lines[-1].strip() == "---":
            out_lines.append("\n")

    out_lines.extend(migrate_body_keep_headings(body, deck_tag))
    return "".join(out_lines)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python migrate_flashcards_to_spaced_repetition_keep_headings.py input.md output.md", file=sys.stderr)
        return 2

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    text = in_path.read_text(encoding="utf-8")
    migrated = migrate_text(text)
    out_path.write_text(migrated, encoding="utf-8")

    print(f"Done. Wrote migrated file to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
