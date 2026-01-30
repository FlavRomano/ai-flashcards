# Lesson: Adversarial Search (Game Theory in AI)

## Introduction: What are we studying? (Slides 1-3)
Welcome to the module on **Search in Games**. Up until now in the course, you’ve likely studied "search" (like A* or DFS) as a solitary activity—a robot finding a path through a maze. Nothing in the maze fights back.

Today, that changes. We are entering **Adversarial Search**.
This applies to **Competitive Games**, specifically those that are:
1.  **Zero-sum:** If I win (+1), you lose (-1). The total utility is 0.
2.  **Turn-based:** We alternate moves.
3.  **Perfect Information:** We can both see the entire board (like Chess or Tic-Tac-Toe, unlike Poker where cards are hidden).

**The Goal:** We want to find a strategy (a conditional plan) that tells us what to do for *every possible move* the opponent makes.

---

## Chapter 1: The Game Tree (Slides 4-6)
To an AI, a game is just a graph.
*   **Nodes** are states of the game (board configurations).
*   **Edges** are the legal moves.

We visualize this as a **Game Tree**.
*   **Root:** The starting position.
*   **Leaves:** The end of the game (Win/Loss/Draw).

**The Players:**
We call our AI **MAX**. We call the opponent **MIN**.
*   **MAX** wants to maximize the final score.
*   **MIN** wants to minimize the score (because a low score for MAX is a win for MIN).

**The Problem of Size:**
Look at Slide 6. A simple game like Tic-Tac-Toe has about 360,000 states. Chess has $10^{40}$. We cannot physically build the whole tree for Chess. Keep this in mind; it’s why we will need "Pruning" and "MCTS" later.

---

## Chapter 2: The Minimax Algorithm (Slides 7-11)
How do we play perfectly if the tree is small enough (like Tic-Tac-Toe)? We use **Minimax**.

### The Logic
We assume the opponent plays **perfectly**.
*   If we are at a "MAX" node (our turn), we look at our children and pick the **highest** value.
*   If we are at a "MIN" node (opponent's turn), we assume they will pick the move that gives us the **lowest** value.

### The Algorithm (Depth-First Search)
1.  Dive all the way down to the **terminal states** (leaves).
2.  Assign utility values (e.g., +1 for Win, -1 for Loss, 0 for Draw).
3.  **Backtrack** up the tree:
    *   Pass the *minimum* value up if it's MIN's level.
    *   Pass the *maximum* value up if it's MAX's level.

**Complexity (Slide 9):**
*   **Time:** $O(b^m)$ (Exponential). If the game is deep ($m$) and has many moves ($b$), this takes forever.
*   **Space:** $O(bm)$ (Linear). We only need to store the current path.

**Suboptimal Opponents (Slide 11):**
*Note:* Minimax assumes the opponent is a genius (Carlsen). If the opponent is bad, Minimax still plays safely. Sometimes, a "risky" move would beat a bad player faster, but Minimax will settle for a safe draw if it sees a 0.0001% chance the opponent finds a perfect counter-move.

---

## Chapter 3: Optimization - Alpha-Beta Pruning (Slides 13-20)
Since we can't search the whole tree for Chess ($35^{80}$ states), we need to cut corners. This is called **Pruning**.

**The Concept:** "If I already found a winning move, I don't need to waste time checking if other moves are 'slightly less winning' or 'terrible'."

We introduce two variables:
*   $\alpha$ (Alpha): The best (highest) value MAX has found so far.
*   $\beta$ (Beta): The best (lowest) value MIN has found so far.

**The Rule (Slide 18):**
If you are looking at a branch and you realize that the opponent (MIN) has an option that is worse than a move you (MAX) already found elsewhere, **stop looking**. You will never reach this branch because the opponent won't let you, or you won't choose it.

*   **Pruning Logic:** If $\alpha \ge \beta$, prune the rest of the children.

**Does it change the result?**
No! That is the beauty of it. It finds the exact same "perfect" move as Minimax, just faster.
*   **Efficiency:** In the best case (if you check the best moves first), it effectively doubles the depth you can search.

Here is the step-by-step explanation of the Alpha-Beta Pruning example shown in **Slides 14–17**.

To follow this, remember the **Golden Rule**:
*   **MAX (Triangle nodes):** Wants the highest number. Keeps track of $\alpha$ (the guaranteed minimum score it can get).
*   **MIN (Inverted Triangle nodes):** Wants the lowest number. Keeps track of $\beta$ (the guaranteed maximum score it can give).

We are looking at the values as an interval $[\alpha, \beta]$.
*   Initially, we know nothing, so the interval is $[-\infty, +\infty]$.

---

### Step 1: The Left Branch (Slides 14 & 15)
**Current Node:** B (MIN node)
**Parent Node:** A (MAX node)

1.  The search goes down the left side first (Depth-First Search). It hits the leaf with value **3**.
2.  Node **B** is a **MIN** player. It sees a 3.
3.  Node B now knows: *"The worst I can do is 3. I might find something smaller (better for me), but I will definitely not accept anything bigger than 3."*
    *   In the notation on **Slide 14**, B's range becomes $[-\infty, 3]$.
4.  Node B checks its next child (value **12**).
5.  **Decision:** MIN wants the smallest number. 3 is smaller than 12. So B ignores the 12 and keeps the **3**.
6.  **Node B resolves to the value 3.**

---

### Step 2: Update the Root (Slide 16)
**Current Node:** A (MAX node)

1.  Now we move back up to the root, **A**.
2.  Node A is a **MAX** player. It just received a value of **3** from its left child (B).
3.  Node A says: *"Okay, if I go left, I get a 3. So now I know that my final score will be **at least** 3. It could be higher if the right branch is amazing, but it won't be lower."*
4.  In the notation on **Slide 16**, A's range updates from $[-\infty, +\infty]$ to **$[3, +\infty]$**.
    *   This **3** is our **Alpha ($\alpha$)**.

---

### Step 3: The Right Branch & The Prune (Slide 17)
**Current Node:** C (MIN node)

This is the critical moment.

1.  Search goes down to Node **C**.
2.  Node C visits its first child (leaf with value **2**).
3.  Node C is a **MIN** player. It sees a 2.
4.  Node C says: *"I found a 2! Since I am a MIN player, my final value for this node will be **2 or something even smaller**."*
5.  In the notation, C's range becomes **$[-\infty, 2]$**.

**The Logic Check (The Pruning):**
Now, let's look at the situation from the Root (A)'s perspective:
*   **Root A (MAX)** has already secured a **3** from the left side.
*   **Node C (MIN)** is promising a value that is **at most 2** (because C will choose the 2, or something smaller if it finds it).

**The Decision:**
Root A thinks: *"Why would I ever choose path C? Path C gives me a 2 (or worse). Path B gives me a 3. Since I am MAX, I prefer 3. I don't care what the other children of C are. Even if C has a child with value -100, C (being MIN) would choose that over the 2, which is even worse for me!"*

**Result:**
*   We **PRUNE** the rest of Node C's children (the dotted triangles in Slide 17).
*   We do not even look at them. We save time.
*   We immediately return the value up to A.

---

### In Plain English (The Analogy)
Imagine you are MAX, and you want to buy a car for the **highest** resale value possible.

1.  **Dealer B** offers you a car worth **$3,000**. You lock that in as your backup plan ($\alpha = 3000$).
2.  You go to **Dealer C**. You ask to see their first car.
3.  Dealer C (who is your enemy/MIN) shows you a car worth **$2,000**.
4.  Dealer C says: *"I have other cars in the back, do you want to see them? But remember, I (MIN) will force you to take the cheapest car I have."*
5.  You say: *"Stop. I don't need to see the cars in the back. You already showed me a $2,000 car. Since you force me to take the cheapest one, the best I can hope for here is $2,000. I already have a $3,000 offer from Dealer B. **I'm leaving.**"*

---

## Chapter 4: Imperfect Solutions - Heuristics (Slide 21)
Even with Pruning, Chess is too deep to reach the end. So, we stop early (Cutoff).
Instead of reaching "Checkmate," we stop at depth 10 and ask a **Heuristic Function**: *"Does this board look good?"*
*   *Chess Heuristic:* Value = (My Pieces) - (Opponent Pieces).

**Two Strategies:**
1.  **Type A:** Check *every* move to depth $D$. (Safe, standard).
2.  **Type B:** Ignore "obviously bad" moves to search deeper on promising ones. (Risky, but necessary for complex games).

**The Risk (Horizon Effect):**
The heuristic might say "You are winning!" because you have a Queen. But if we looked just **one** move deeper, we'd see the Queen is about to be captured. The AI is "blind" beyond its horizon.

---

## Chapter 5: Monte-Carlo Tree Search (MCTS) (Slides 22-28)
*Teacher's Note: This is the modern revolution. This is how AlphaGo works.*

For games like Go, the branching factor is too huge for Alpha-Beta. We need a different approach. Instead of calculating *exact* values, we estimate them using **Probability**.

### The Process (Slide 23)
We build the tree gradually, focusing only on "interesting" paths.
1.  **Selection:** Start at the root and pick a path down to a leaf using a "Smart Policy" (UCT).
2.  **Expansion:** Add a new child node to the tree.
3.  **Simulation (Rollout):** From that new node, play random moves until the game ends. Who won?
4.  **Backpropagation:** Update the nodes on the path:
    *   Increase "Total Visits" ($N$) by 1.
    *   Increase "Total Wins" ($U$) only for the player who won.

### The "Smart Policy": UCT (Slide 25)
How do we choose which node to explore? We use the formula:
$$UCB1 = \text{Average Win Rate} + \text{Exploration Factor}$$

*   **Exploitation:** "This move has won a lot before, let's do it again."
*   **Exploration:** "We haven't visited this move much, let's try it to see if it's a hidden gem."

This balances the AI so it doesn't get stuck doing one thing, but also doesn't waste time on random garbage.

---

## Chapter 6: Stochastic Games (Slides 29-30)
What if we play Backgammon or Poker? There is luck (Dice/Cards).
We add a new type of node: **Chance Nodes** (Circles).

Instead of taking the Max or Min, the value of a Chance node is the **Weighted Average** (Expected Value) of its children.
*   *Example:* If Move A leads to a 50% chance of winning (+100) and 50% chance of losing (-100), the value is 0.

---

## Summary & Exam Takeaways
1.  **Minimax** is perfect but slow ($O(b^m)$).
2.  **Alpha-Beta Pruning** is mathematically identical to Minimax but faster because it ignores irrelevant branches.
3.  **Heuristics** allow us to stop searching early by estimating board value, but risk the **Horizon Effect**.
4.  **MCTS** is best for huge games (Go). It uses random simulations + UCT to balance **Exploration vs. Exploitation**.

