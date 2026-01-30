## **1. Introduction to Genetic Algorithms (GAs)**
Genetic Algorithms are "general-purpose" optimization protocols inspired by biological evolution. While originally designed for binary representations, they now handle floating-point numbers, strings, trees, and graphs.

### **1.1 The Evolutionary Loop**
The algorithm operates on a **Population** of individuals.
1.  **Genotype:** The internal representation (string, chromosome, code).
2.  **Phenotype:** The actual candidate solution generated from the genotype.
3.  **The Loop:**
    *   **Evaluation:** Calculate fitness.
    *   **Selection:** Choose parents (proportional to fitness).
    *   **Recombination (Crossover):** Combine parents to create offspring.
    *   **Mutation:** Randomly alter offspring.

### **1.2 Crossover Operators**
Recombination mixes genetic material.
*   **1-Point Crossover:**
    Given chromosomes $A$ and $B$ of length $n$, select split point $k \in [1, \dots, n-1]$.
    *   Offspring 1: Takes head of $A$ ($1:k$) and tail of $B$ ($k+1:n$).
    *   Offspring 2: Takes head of $B$ ($1:k$) and tail of $A$ ($k+1:n$).
    *   *Example:* $A=0010, B=1011, k=1 \rightarrow \text{Offspring: } 0011, 1010$.
*   **2-Point Crossover:** Select two split points. Swap the middle segment between parents.

### **1.3 Mutation**
*   **Role:** Maintains diversity and prevents premature convergence.
*   **Mechanism:** Randomly mutate an element (e.g., bit flip) with **low probability**.
*   *Note:* Unlike Evolution Strategies (ES) where mutation is the primary driver, in GAs mutation is rare; crossover is the primary driver.

---

## **2. Input Encoding & Representation**
The encoding is the most critical design choice. A "wrong" encoding can make the search space disjoint or deceptive.

### **2.1 The Hamming Cliff Problem**
Using standard binary encoding for integers can introduce artificial difficulty.
*   $6 \rightarrow 0110$
*   $7 \rightarrow 0111$ (1 bit flip)
*   $8 \rightarrow 1000$ (4 bit flips!)
**Problem:** To move from 7 to 8, *every* bit must change simultaneously. This is a "Hamming Cliff."
**Solution:** Use **Gray Coding**, where consecutive integers differ by exactly one bit.

### **2.2 Direct vs. Indirect Encodings**
*   **Direct Encoding:** 1-to-1 mapping. Each gene corresponds to one feature in the phenotype.
    *   *Pros:* Easy to design.
    *   *Cons:* Does not scale (parameter explosion); cannot represent modularity or symmetry.
*   **Indirect (Developmental) Encoding:** Genotype encodes a *rule set* or function that generates the phenotype.
    *   *Pros:* Exploits regularity (e.g., symmetry in a body); highly compressive (small genotype $\rightarrow$ large phenotype).
    *   *Example:* DNA encodes the *process* of growth, not the position of every cell.

### **2.3 CPPNs (Compositional Pattern Producing Networks)**
A popular indirect encoding method.
*   **Concept:** The "individual" is a mathematical function network $f$.
*   **Input:** Geometric coordinates (e.g., $x, y$).
*   **Output:** Phenotypic value (e.g., pixel color, connection weight).
*   **Mechanism:** Composes simple activation functions (Gaussian, Sine, Abs, Linear) to create complex, symmetric, and repeating patterns.

---

## **3. Neuroevolution: NEAT**
**NEAT** (NeuroEvolution of Augmenting Topologies) is the standard for evolving Neural Networks (NNs). Unlike standard Deep Learning (which optimizes weights for a fixed architecture), NEAT evolves **both weights and topology**.

### **3.1 NEAT Mechanisms**
1.  **Complexification:** Start with minimal networks (inputs connected directly to outputs). Gradually add complexity only if it improves fitness.
2.  **Genetic Encoding:** A list of Node Genes (Sensor/Hidden/Output) and Connection Genes (In-Node, Out-Node, Weight, Enabled bit, **Innovation Number**).
3.  **Mutation:**
    *   *Add Connection:* Link two previously unconnected nodes.
    *   *Add Node:* Split an existing connection (disable old, create two new ones flanking the new node).

### **3.2 Solving the Crossover Problem**
Problem: How do you cross over two neural networks with different topologies?
**Solution: Innovation Numbers.**
*   Every time a new structural mutation occurs globally, it is assigned a unique incrementing integer (Innovation Number).
*   When crossing over, genes with the same Innovation Number are "matching" (homologous) and can be aligned perfectly.

### **3.3 Speciation (Protecting Innovation)**
New structural mutations (like a new node) usually perform poorly initially (unoptimized weights). In a standard GA, they would die out immediately.
**Solution:** NEAT groups individuals into **Species**. Competition is restricted to the same species.

**Distance Formula ($\delta$):** Defines if two genomes belong to the same species.
$$ \delta = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \cdot \Delta W $$
*   $E$: Number of **Excess** genes (genes outside the range of the other parent).
*   $D$: Number of **Disjoint** genes (genes within the range but missing in one).
*   $\Delta W$: Average weight difference of matching genes.
*   $N$: Total number of genes.

**Explicit Fitness Sharing:**
The fitness of individual $i$ in species $s$ is adjusted:
$$ f'_i = \frac{f_i}{|s|} $$
*   This penalizes large species, preventing one species from taking over the entire population.

### **3.4 HyperNEAT**
Combines CPPNs with NEAT to evolve massive NNs.
*   **Substrate:** A geometric grid of neurons.
*   **CPPN Input:** Coordinates of two neurons $(x_1, y_1)$ and $(x_2, y_2)$.
*   **CPPN Output:** The weight $w$ of the connection between them.
*   *Result:* Patterns in the CPPN (symmetry, repetition) become patterns in the Neural Network's weights (e.g., a visual cortex with repeated filters).

---

## **4. The Myth of the Objective**
Traditional optimization assumes "hill-climbing" towards an objective works.
*   **Deception:** In complex spaces, the path to the global optimum often requires passing through lower-fitness regions (valleys).
*   **Picbreeder Insight:** An interactive evolution experiment. Users evolved images like "skulls" or "butterflies" but admitted they *could not* have found them if they set out with that specific goal.
*   **Stepping Stones:** The intermediate steps (stepping stones) to a complex solution rarely resemble the final solution.

---

## **5. Diversity-Driven Search Algorithms**

### **5.1 Novelty Search**
Abandon the objective function.
*   **Goal:** Maximize behavioral novelty.
*   **Method:**
    1.  Define a **Behavior Characterization (BC)** (e.g., the final $(x,y)$ coordinate of a robot).
    2.  Maintain an **Archive** of past behaviors.
    3.  Compute **Sparseness ($\rho$)** as fitness.
    
**Sparseness Formula:**
$$ \rho(x) = \frac{1}{k} \sum_{i=1}^{k} d(x, n_i) $$
*   $d(x, n_i)$: Distance between individual $x$ and its $i$-th nearest neighbor in the archive/population.
*   If $\rho(x) > \rho_{min}$, add $x$ to the archive.

### **5.2 Quality Diversity (QD)**
Seek a set of solutions that are **maximally diverse** but also **high performing**.

**Algorithm: MAP-Elites (Multi-dimensional Archive of Phenotypic Elites)**
1.  **Define Dimensions:** Create a grid based on features (e.g., Height vs. Weight).
2.  **Generate Offspring:** Randomly mutate a parent.
3.  **Evaluate:** Get Fitness (Performance) and Descriptor (Bin location).
4.  **Update Grid:**
    *   If bin is empty $\rightarrow$ Place offspring there.
    *   If bin is occupied $\rightarrow$ Replace if offspring has **higher fitness**.
    
**Algorithm: NSLC (Novelty Search with Local Competition)**
*   Uses Novelty Search for diversity.
*   Uses a "Local Quality" score: The percentage of nearest neighbors (k-NN) that the individual outperforms.
*   Does not require a predefined grid (niches are adaptive).

**Evaluation Metric: QD-Score**
$$ \text{QD-Score} = \sum_{i=1}^{\#bins} Q_i $$
*   Sum of fitnesses ($Q_i$) of all filled bins. High score requires filling many bins (Diversity) with good solutions (Quality).

---

## **6. Evolvability & Open-Endedness**

### **6.1 Evolvability**
The capacity of an individual's genome to generate adaptive phenotypic variation.
*   **Evolvability Search:** Select parents not based on *their* fitness, but on how diverse their *offspring* are.
*   **Evolvability ES (Evolution Strategies):** Optimizes for evolvability using gradients.
    *   Maximize the variance of the behavior distribution.
    *   **Objective Function:**
        $$ F(\theta) = \sum_j E_{z \sim \pi}[(B_j(z) - \mu_j)^2] $$
        (Sum of variances of behavior component $B_j$ around mean $\mu_j$).