# Summary
| **Section**             | **Difficulty Level** | **Difficulty Score (1-5)** | **Why?**                                                                    |
| ----------------------- | -------------------- | -------------------------- | --------------------------------------------------------------------------- |
| **Search**              | Easy                 | 🟢 1.8                     | High-level fundamentals; mostly intuitive algorithms.                       |
| **Local Search**        | Medium-Easy          | 🟡 2.2                     | Introduces stochastic elements and complex data structures.                 |
| **CSP**                 | Medium               | 🟠 2.8                     | Higher logic density; requires understanding of constraint propagation.     |
| **Games**               | Hard                 | 🔴 3.8                     | Recursive complexity (Minimax) and high-level sampling (MCTS).              |
| **Evo 1 & 2**           | Hard                 | 🔴 4.2                     | Complex parameter tuning (CMA-ES) and advanced neural architectures (NEAT). |
| **Artificial Life**     | Medium-Hard          | 🟠 3.5                     | Combines cellular physics, convolution math, and chaos theory.              |
| **Propositional Logic** | Medium               | 🟠 2.9                     | Heavy on formal proofs and systematic inference algorithms.                 |
| **FOL**                 | Expert               | ⚫ 4.8                     | Most abstract; requires mastery of unification and semi-decidability.       |
| **Planning**            | Medium-Hard          | 🟠 3.2                     | Abstract state spaces and complex heuristic design (PDDL).                  |
| **Probability**         | Medium               | 🟠 3.0                     | Foundational but requires strong mathematical intuition.                    |
| **Bayesian Networks**   | Hard                 | 🔴 4.0                     | High mathematical overhead for exact and approximate inference.             |
| **Reasoning Over Time** | Hard                 | 🔴 3.9                     | Temporal math; keeping track of distributions over time (Viterbi).          | 
|**Multi-Agent**|Medium|🟠 2.7|Conceptual shift to game theory and social welfare metrics.|

# First part
## Search

| Name             | Type       | Difficulty |
| ---------------- | ---------- | ---------- |
| BFS              | Algorithm  | 1          |
| DFS              | Algorithm  | 1          |
| Djikstra         | Algorithm  | 2          |
| Heuristics       | Definition | 1          |
| Greedy search    | Algorithm  | 1          |
| A*               | Algorithm  | 1          |
| Weighted A*      | Algorithm  | 1          |
| Optimality of A* | Proof      | 1          |

## Local Search
| Name                | Type      | Difficulty |
| ------------------- | --------- | ---------- |
| Hill climbing       | Algorithm | 1          |
| Simulated annealing | Algorithm | 2          |
| Local Beam Search   | Algorithm | 2          |
| AND-OR Search Tree  | DS        | 2          |
| AND-OR DFS          | Algorithm | 2          |

## Constraint Satisfaction Problem (CSP)
| Name                        | Type                | Difficulty |
| --------------------------- | ------------------- | ---------- |
| Factored Representation     | Definition          | 1          |
| Map coloring                | Problem Description | 1          |
| Constraint Graph            | Definition          | 1          |
| Backtracking Search         | Algorithm           | 2          |
| Minimum Remaining Values    | Algorithm           | 1          |
| Degree heuristic            | Algorithm           | 1          |
| Least Constraining values   | Algorithm           | 1          |
| Forward checking            | Algorithm           | 2          |
| Arc consistency             | Definition          | 2          |
| Maintaining Arc Consistency | Algorithm           | 1          | 

## Games
| Name                     | Type                | Difficulty |
| ------------------------ | ------------------- | ---------- |
| Min-Max problem          | Problem description | 2          |
| Minimax                  | Algorithm           | 3          |
| $\alpha$-$\beta$ pruning | Definition          | 2          |
| Monte-Carlo Tree Search  | Algorithm           | 3          |
| UCT                      | Definition          | 3          |
| Expected Minimax         | Definition          | 1           |

# Second part (EVO)
## Evo 1
| Name                               | Type       | Difficulty |
|:---------------------------------- |:---------- |:---------- |
| Artificial Life (Soft/Hard/Wet)    | Definition | 1          |
| EA Skeleton                        | Algorithm  | 1          |
| Genetic Algorithms (GA)            | Definition | 1          |
| Genetic Programming (GP)           | Definition | 1          |
| Evolution Strategies (ES)          | Algorithm  | 2          |
| Strategy Parameters ($\sigma$)     | Definition | 2          |
| $(\mu, \lambda)$ Selection (Comma) | Mechanism  | 2          |
| $(\mu + \lambda)$ Selection (Plus) | Mechanism  | 1          |
| CMA-ES                             | Algorithm  | 3          |
| Rank-$\mu$ Update                  | Mechanism  | 3          |
| Rank-One Update                    | Mechanism  | 3          |
| Evolution Path                     | Definition | 2          |

## Evo 2
| Name                           | Type                    | Difficulty |
|:------------------------------ |:----------------------- |:---------- |
| Input Encoding (Hamming Cliff) | Problem Description     | 1          |
| Direct vs. Indirect Encoding   | Definition              | 1          |
| CPPN                           | Definition/Architecture | 2          |
| NEAT                           | Algorithm               | 3          |
| Innovation Number              | Mechanism               | 2          |
| Speciation (NEAT)              | Mechanism               | 2          |
| HyperNEAT                      | Algorithm               | 3          |
| Novelty Search                 | Algorithm               | 2          |
| Sparseness Metric ($\rho$)     | Definition              | 2          |
| Quality Diversity (QD)         | Definition              | 1          |
| MAP-Elites                     | Algorithm               | 2          |
| Evolvability Search            | Algorithm               | 2          |
| Evolvability ES                | Algorithm               | 3          |

## Artificial Life
| Name                              | Type                | Difficulty |
|:--------------------------------- |:------------------- |:---------- |
| Complex Systems (Emergence)       | Definition          | 1          |
| Tierra / Avida                    | Problem Description | 1          |
| Logistic Map (Chaos Theory)       | Definition          | 2          |
| Cellular Automata (CA)            | Definition          | 1          |
| Elementary CA (ECA)               | Mechanism           | 1          |
| Wolfram Rules (Rule 110, etc.)    | Mechanism           | 2          |
| Wolfram Classes (Type I - IV)     | Definition          | 2          |
| Universal Computation (Rule 110)  | Proof/Definition    | 2          |
| Game of Life (GoL)                | Problem Description | 1          |
| Glider Gun / Life-like structures | Definition          | 1          |
| Lenia (Continuous CA)             | Definition          | 2          |
| Kernel Convolution ($K \star A$)  | Mechanism           | 3          |
| Growth Mapping $G(U)$             | Mechanism           | 2          |
| Solitons                          | Definition          | 2          |
| Neural Cellular Automata (NCA)    | Architecture        | 2          |
| Morphogenesis                     | Definition          | 1          |
| Perception Phase (Sobel Filters)  | Mechanism           | 2          |
| Stochastic Update                 | Mechanism           | 1          |
| Sample Pool (Stability Training)  | Mechanism           | 3          |
| Regeneration / Self-Repair        | Property            | 2          |

# Logic
## Propositional Logic
| Name                      | Type                 | Difficulty |
|:------------------------- |:-------------------- |:---------- |
| Knowledge-Based Agent     | Definition           | 1          |
| KB (Knowledge Base)       | Definition           | 1          |
| Tell-Ask Paradigm         | Mechanism            | 1          |
| Wumpus World (PEAS)       | Problem Description  | 1          |
| Syntax vs. Semantics      | Definition           | 1          |
| Models / Possible Worlds  | Definition           | 2          |
| Entailment ($\models$)    | Definition           | 2          |
| Model Checking            | Definition/Mechanism | 2          |
| Validity & Satisfiability | Definition           | 2          |
| Soundness & Completeness  | Property             | 2          |


| Name                                                                     | Type       | Difficulty |
|:------------------------------------------------------------------------ |:---------- |:---------- |
| Propositional Symbols ($P, Q$)                                           | Definition | 1          |
| Logical Connectives ($\neg, \wedge, \lor, \Rightarrow, \Leftrightarrow$) | Mechanism  | 1          |
| Truth Tables                                                             | Mechanism  | 1          |
| Inference by Enumeration                                                 | Algorithm  | 2          |
| Logical Equivalences (De Morgan, etc.)                                   | Proof/Rule | 2          |
| CNF (Conjunctive Normal Form)                                            | Definition | 2          |
| Resolution Rule                                                          | Mechanism  | 2          |
| Resolution Inference                                                     | Algorithm  | 3          |
| Horn Clauses                                                             | Definition | 2          |
| Modus Ponens                                                             | Mechanism  | 1          |
| Forward Chaining                                                         | Algorithm  | 3          |
| Backward Chaining                                                        | Algorithm  | 3          |
| Expressiveness Limitation                                                | Property   | 1          |

## FOL
| Name                             | Type                | Difficulty |
|:-------------------------------- |:------------------- |:---------- |
| Syntax (Terms, Atoms, Sentences) | Definition          | 1          |
| Quantifiers ($\forall, \exists$) | Definition          | 1          |
| Model & Interpretation           | Definition          | 2          |
| Closed-World Assumption          | Definition          | 1          |
| Universal Instantiation (UI)     | Mechanism           | 1          |
| Existential Instantiation (EI)   | Mechanism           | 2          |
| Skolemization                    | Mechanism           | 2          |
| Propositionalization             | Mechanism           | 1          |
| Herbrand's Theorem               | Theorem             | 2          |
| Semi-decidability of FOL         | Property            | 2          |
| Unification                      | Mechanism           | 2          |
| Standardizing Apart              | Mechanism           | 1          |
| Generalized Modus Ponens (GMP)   | Inference Rule      | 2          |
| Definite Clauses                 | Definition          | 1          |
| Forward Chaining                 | Algorithm           | 1          |
| Backward Chaining                | Algorithm           | 2          |
| Prolog (Logic Programming)       | Language/Definition | 1          |
| Resolution (FOL)                 | Algorithm           | 3          |
| CNF Conversion (FOL)             | Mechanism           | 3          |
| Ontologies                       | Definition          | 1          |


## Planning
| Name                                | Type       | Difficulty |
|:----------------------------------- |:---------- |:---------- |
| Classical Planning (PDDL)           | Definition | 1          |
| Action Schema (Precond/Effect)      | Mechanism  | 1          |
| Forward State-space Search          | Algorithm  | 1          |
| Backward Search (Relevant Actions)  | Algorithm  | 1          |
| Relaxed Problem Heuristics          | Definition | 2          |
| Ignore Preconditions Heuristic      | Mechanism  | 2          |
| Ignore Delete List Heuristic        | Mechanism  | 2          |
| Symmetry Reduction                  | Mechanism  | 2          |
| State Abstraction                   | Mechanism  | 2          |
| Hierarchical Planning (HLA)         | Algorithm  | 2          |
| Sensorless Planning (Belief States) | Definition | 3          |
| Online Planning (Monitoring)        | Algorithm  | 1          |
| Critical Path Method (CPM)          | Algorithm  | 2          |
| Minimum Slack Heuristic             | Algorithm  | 2          |

# Probability 
## Uncertainty
| Name                              | Type       | Difficulty |
|:--------------------------------- |:---------- |:---------- |
| Sources of Uncertainty            | Definition | 1          |
| Bayesian vs. Frequentist View     | Definition | 1          |
| Utility & Decision Theory         | Definition | 1          |
| Principle of MEU                  | Definition | 1          |
| Axioms of Probability             | Definition | 1          |
| Joint Probability Distribution    | Definition | 2          |
| Marginalization                   | Mechanism  | 2          |
| Independence / Conditional Indep. | Definition | 2          |
| Bayes' Rule                       | Formula    | 2          |
| Naïve Bayes Model                 | Model      | 2          |
| Frontier-based Inference          | Mechanism  | 3          |

## Bayesian Networks

| Name                                | Type       | Difficulty |
|:----------------------------------- |:---------- |:---------- |
| Bayesian Network (DAG)              | Definition | 1          |
| Conditional Probability Table (CPT) | Definition | 1          |
| Global Semantics (Chain Rule)       | Definition | 2          |
| Markov Blanket                      | Definition | 2          |
| Noisy-OR                            | Mechanism  | 2          |
| Hybrid Bayesian Networks            | Definition | 2          |
| Linear Gaussian / Sigmoid           | Mechanism  | 2          |
| Inference by Enumeration            | Algorithm  | 2          |
| Variable Elimination                | Algorithm  | 3          |
| Factors (Sum / Product)             | Mechanism  | 2          |
| Polytrees (Singly-connected)        | Definition | 1          |
| Direct Sampling                     | Algorithm  | 1          |
| Rejection Sampling                  | Algorithm  | 2          |
| Importance Sampling                 | Algorithm  | 3          |
| Causal Networks                     | Definition | 2          |
| The `do()` Operator (Intervention)  | Mechanism  | 3          |
| Graph Surgery                       | Mechanism  | 2          |

## Probabilistic Reasoning Over Time
| Name                            | Type       | Difficulty |
|:------------------------------- |:---------- |:---------- |
| Concept Drift (Virtual vs Real) | Definition | 1          |
| Markov Chain                    | Model      | 1          |
| Stationarity Assumption         | Definition | 1          |
| First-order Markov Assumption   | Definition | 1          |
| Hidden Markov Model (HMM)       | Model      | 2          |
| Transition & Sensor Models      | Definition | 1          |
| Filtering (Forward Message)     | Algorithm  | 2          |
| Prediction (Stationary Dist.)   | Task       | 2          |
| Smoothing (Forward-Backward)    | Algorithm  | 3          |
| Likelihood of Evidence          | Task       | 2          |
| Viterbi Algorithm               | Algorithm  | 3          |

## Multi agent
| Name                                     | Type                | Difficulty |
| :--------------------------------------- | :------------------ | :--------- |
| Benevolent Agent Assumption              | Definition          | 1          |
| Interleaved Execution Model              | Mechanism           | 2          |
| True Concurrency (Joint Actions)         | Definition          | 2          |
| Concurrent Action Constraints            | Definition          | 2          |
| Plan Recognition                         | Mechanism           | 2          |
| Normal Form Games                        | Definition          | 1          |
| Pure vs. Mixed Strategy                  | Definition          | 1          |
| Dominant Strategy                        | Definition          | 1          |
| Nash Equilibrium                         | Definition          | 2          |
| Pareto Optimality                        | Definition          | 1          |
| Social Welfare (Utilitarian/Egalitarian) | Definition          | 1          |
| Prisoner's Dilemma                       | Problem Description | 1          |
| Equilibrium Search Complexity            | Complexity          | 2          |