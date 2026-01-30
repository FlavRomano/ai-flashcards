### **Part 1: Motivation and the Philosophy of Artificial Life**

**(Slide 1)**
Good morning, everyone. Welcome back. Today we are diving into a fascinating subfield of AI: **Evolutionary Optimization**. We are going to look at how we can borrow the fundamental engine of biological life—evolution—and apply it to solve complex computational problems.

**(Slide 2)**
Let's start with the motivation. Why do we look at biology? Because biological life is difficult, yet it persists and adapts. This leads us to the concept of **Artificial Life (ALife)**. As defined by Langton, ALife attempts to understand the essential properties of living systems by synthesizing life-like behavior.

We can categorize ALife into three types:
1.  **Soft Artificial Life:** This is what we do mostly—computer simulations, software agents.
2.  **Hard Artificial Life:** Hardware implementations. Think of soft robots where we co-evolve the "brain" (controller) and the "body" (morphology) simultaneously.
3.  **Wet Artificial Life:** Synthesis of biological systems from biochemical substances (artificial cells).

Crucially, this isn't always strictly an engineering effort. We aren't always trying to minimize an error margin. Sometimes, we just want to understand *how* complex behaviors emerge.

**(Slide 3)**
Historically, pioneers like John von Neumann (Cellular Automata) and Norbert Wiener (Cybernetics) laid the groundwork. But Christopher Langton really framed the field in 1989 with a profound idea: Biology studies "life as we know it" (carbon-based, Earth-evolved). Artificial Life allows us to study **"life as it could be."** It expands the theoretical bounds of biology.

**(Slide 4)**
So, how do we simulate this? We need to replicate the **origins of life**.
We treat life as an **iterative process**. Infinite loops are powerful. We need:
1.  **Initial Conditions:** The environment and the start state.
2.  **An Evolution Algorithm:** The rules for how life progresses, diversifies, and descends from ancestors.

**(Slide 5)**
This draws directly from biological literature—Darwin’s *Origin of Species*, Dawkins’ *The Selfish Gene*, and others. These works describe the mechanism we want to copy.

**(Slide 6)**
To simulate **Natural Selection**, we need three necessary and sufficient conditions:
1.  **Differential Reproduction:** Not everyone reproduces at the same rate. The environment favors certain traits.
2.  **Heredity:** Traits must be passed to children.
3.  **Variation:** The population cannot be identical; there must be diversity.

If we have these, advantageous traits survive. However, we must be careful. If we only select the absolute best, the population converges to a homogenous state (clones) and evolution stops.

**(Slide 7)**
Evolution isn't just a slow, steady climb.
*   **Punctuated Equilibria:** Evolution can happen in rapid bursts after long periods of stasis.
*   **Adaptation:** A feature becomes better at a specific task.
*   **Exaptation:** This is cool—a trait evolved for one reason is suddenly used for a completely different purpose (e.g., feathers were likely for warmth before they were used for flight).

**(Slide 8)**
To maintain the diversity I mentioned, we rely on:
*   **Random Mutation:** Creating new genes.
*   **Recombination (Crossover):** Shuffling existing genes (like sexual reproduction).
*   **Natural Selection:** Driven by **Fitness**—how good a genotype is at passing on its genes.
This is a **Divergent Process**. It creates novelty rather than collapsing immediately.

---

### **Part 2: The Digital Transition and Evolutionary Algorithms**

**(Slide 9-10)**
Now, let’s move to **Digital Evolution**. If we can simulate the initial conditions and the algorithm, we can "create" artificial life. However, we have a problem: **Approximation**. Biological systems are chaotic. Even tiny errors in our approximation of initial conditions lead to massive divergence later.

**(Slide 11)**
Despite this, we have been using **Evolutionary Algorithms (EAs)** since the 1950s to solve optimization problems. We simulate those three pillars: Variation, Differential Reproduction, and Heredity.

**(Slide 12)**
Here is the **Skeleton of an Evolutionary Algorithm**:
1.  **Initialize Population ($P_0$):** A set of individuals (solutions) with $N$ features (genes). These features could be bit-strings, real numbers, or graphs.
2.  **Evaluate Fitness:** How good is each individual?
3.  **Loop ($t=1, 2, ...$):**
    *   **Select Parents:** Based on fitness.
    *   **Recombine:** Mix parents to make children.
    *   **Mutate:** Randomly alter features.
    *   **Evaluate:** Check the fitness of the new batch.
    *   **Select Survivors:** Keep $K$ individuals for the next generation.

**(Slide 13)**
There are many variants.
*   **Selection:** Do parents survive? Or do we replace them entirely?
*   **Exploitation:** Do we hill-climb (only keep the very best)?
*   **Representation:** Are we mutating bits or real numbers?

**(Slide 15)**
We categorize EAs into three main families:
1.  **Evolution Strategies (ES):** Distribution-based. We work with real-valued vectors. This is our focus today.
2.  **Genetic Algorithms (GA):** Population-based, usually bit-strings (0s and 1s). Recombination is the main driver.
3.  **Genetic Programming (GP):** We evolve code or instructions (like syntax trees) to generate programs.

**(Slides 16-17)**
A famous example is **Karl Sims' Virtual Creatures (1994)**. He used evolution to create 3D block creatures that learned to walk, swim, and jump without being told *how*—simply by being rewarded for distance traveled.

**(Slide 18)**
But be warned: **Evolution cheats.** This is known as "specification gaming."
If you evolve code to sort a list, the algorithm might realize that an *empty* list is technically sorted, and just delete all the data.
If you ask it to match a text file, it might delete the target file so the comparison returns "true."
It also produces **Bloat**: huge amounts of junk code that do nothing, simply to protect the important code from mutation.

---

### **Part 3: Evolution Strategies (ES) and Black-Box Optimization**

**(Slide 19)**
Let's get formal. We are doing **Black-Box Optimization**.
*   We want to maximize a function $f: S \to R$ (usually $S \subset R^n$).
*   **Black Box:** We do **not** have derivatives (gradients). We can only sample points $x$ and get a value $f(x)$.
*   This is perfect for non-convex, rugged landscapes where Gradient Descent fails.

**(Slide 20)**
**Evolution Strategies (ES)** differ from Genetic Algorithms.
*   We operate on **continuous functions**.
*   An individual consists of two parts:
    1.  **Phenotype ($x$):** The decision parameters (the solution).
    2.  **Strategy Parameters ($\sigma$):** The "endogenous" parameters, specifically the **mutation rate**.
*   Crucial Concept: We evolve the mutation rate *along with* the solution.

**(Slide 21)**
In ES, Mutation is usually adding **Gaussian Noise**:
$$x_{new} = x + N(0, \sigma^2)$$
If we use an **Isotropic Gaussian**, we have one $\sigma$ for all dimensions (spherical mutation). If we have a diagonal matrix, we have a different $\sigma$ for each dimension (ellipsoidal mutation along axes).

**(Slide 22)**
We define the algorithm using the notation $(\mu, \lambda)$ or $(\mu + \lambda)$.
*   $\rho$: The mixing number (how many parents create one child).
*   If $\rho=1$, it's cloning (asexual).
*   Recombination can be discrete (taking features from one parent or the other) or intermediate (averaging parents).

**(Slide 23)**
Why do we need **Self-Adaptation** of the strategy parameter $\sigma$?
Look at the graph. If $\sigma$ (mutation strength) is constant, the algorithm gets stuck. It can't refine the solution as it approaches the optimum. We need large steps early on (exploration) and tiny steps later (exploitation).

---

### **Part 4: The Math of $(\mu, \lambda)$-ES**

**(Slide 25)**
Let's look at the math for the **$(\mu, \lambda)$-ES**.
*   **Population:** We have $\mu$ parents.
*   **Generation:** We create $\lambda$ offspring, where $\lambda > \mu$.
*   **The Individual:** A pair $(x, \sigma)$.

The generation loop works like this:
1.  **Select** parents (randomly).
2.  **Mutate the Step Size ($\sigma$):**
    $$\sigma^{g+1}_k = \text{recombine}(\sigma^g) \cdot e^{\xi}$$
    where $\xi \sim N(0, 1)$. We mutate the *variance* first!
3.  **Mutate the Solution ($x$):**
    $$x^{g+1}_k = \text{recombine}(x^g) + N(0, (\sigma^{g+1}_k)^2)$$
    We use the *new* step size to mutate the position.

**Selection:** In $(\mu, \lambda)$-ES, we select the best $\mu$ individuals from the $\lambda$ children. **Crucially, the parents are discarded.** They die immediately.

**(Slide 27)**
Contrast this with **$(\mu + \lambda)$-ES**:
Here, we select the best $\mu$ from the **union** of parents and children.
*   **Plus (+):** Elitist. Guaranteed to never get worse.
*   **Comma (,):** Non-elitist. Can get worse.

**(Slide 29)**
Why would we ever use **Comma selection (discarding parents)**?
1.  **Exploration:** It prevents getting stuck in local optima. If the parents are sitting on a local peak, Comma selection forces the population to move away.
2.  **Dynamic/Deceptive Environments:** If the fitness function changes or is deceptive (like a maze where you must move *away* from the goal to find the door), "elitism" traps you. Comma selection allows "forgetting" bad "good" solutions.

**(Slide 30)**
*   If $\mu = \lambda$ in Comma selection: It's a random walk (no selection pressure).
*   If $\mu = \lambda$ in Plus selection: It's pure hill-climbing.

---

### **Part 5: CMA-ES (Covariance Matrix Adaptation)**

**(Slide 32)**
Now we reach the state-of-the-art: **CMA-ES**.
Standard ES uses simple Gaussian noise (spheres). CMA-ES adapts the **Covariance Matrix ($C$)** of the Gaussian distribution.
It shapes the mutation cloud into an ellipsoid that fits the landscape (like a valley). It acts like **momentum** in gradient descent—speeding up on flats, slowing down on turns.

We sample from a multivariate Normal distribution:
$$x \sim N(m^g, \sigma^2 C^g)$$
*   $m^g$: The mean (the current best estimate of the solution).
*   $C^g$: The covariance matrix (the shape of the search).
*   $\sigma$: The global step size.

**(Slide 33)**
**Step 1: Sampling & Update Mean**
We generate offspring:
$$x_k^{g+1} = m^g + \sigma N(0, C^g)$$
We evaluate them and sort them by fitness.
Then we update the mean $m$ by taking a **weighted average** of the best $\mu$ offspring:
$$m^{g+1} = \sum_{i=1}^{\mu} w_i x_i^{g+1}$$
The weights $w_i$ are higher for better solutions.

**(Slide 35)**
**Step 2: Updating the Covariance Matrix ($C$)**
This is the hardest part. The goal is to increase the probability of generating successful steps again.
A simplified view is that we estimate the covariance of the *successful* steps we just took:
$$C^{g+1}_{estimate} \approx (x^{g+1} - m^g)(x^{g+1} - m^g)^T$$
(This is the outer product).

**(Slide 37)**
In practice, we don't just use the current generation. We use **Rank-$\mu$ Update** with exponential smoothing. We mix the old matrix with the new evidence:
$$C^{g+1} = (1 - c_\mu)C^g + c_\mu \sum_{i=1}^{\mu} w_i \left( \frac{x_i^{g+1} - m^g}{\sigma} \right) (\dots)^T$$
*   $c_\mu$ is a learning rate ($0 < c_\mu \leq 1$).
*   This averages the covariance structure over time.

**(Slide 38)**
We can also use a **Rank-One Update**. Instead of using the population average, we use the trajectory of the single best step. In reality, CMA-ES combines both Rank-$\mu$ and Rank-1 updates, and also tracks an **Evolution Path** (a vector summing up steps over generations) to manage step size $\sigma$.

#### Math behind
We are tracking three things that change every generation ($g$):
1.  **$m^g$**: The **Mean** (The center of our search).
2.  **$\sigma$**: The **Step Size** (How wide the overall search is).
3.  **$C^g$**: The **Covariance Matrix** (The *shape* and *orientation* of the search ellipse).

Let’s break down the equations slide by slide.

---

##### 1. Sampling the Population (Slide 32 & 33)
**The Math:**
$$x_k^{g+1} \sim m^g + \sigma N(0, C^g)$$

**The Translation:**
To create a new child ($x_k$), we take the current center ($m^g$) and add noise.
*   $N(0, C^g)$ creates a random vector shaped by the matrix $C$.
*   $\sigma$ scales that shape up or down.

**Key Insight:** If $C$ is the Identity matrix ($I$), the noise is a perfect sphere. If $C$ has off-diagonal numbers (correlations), the noise is an ellipse (e.g., "if $x$ is big, $y$ must also be big").

---

##### 2. Updating the Mean (Slide 33)
**The Math:**
$$m^{g+1} = \sum_{i=1}^{\mu} w_i x_i^{g+1}$$

**The Translation:**
The new center ($m^{g+1}$) is just the **Weighted Average** of the best children.
*   **Selection:** We picked the top $\mu$ children out of $\lambda$.
*   **Weights ($w_i$):** We don't treat all survivors equally. The #1 survivor gets a higher weight ($w_1$) than the #5 survivor ($w_5$).
*   **Normalization:** $\sum w_i = 1$.

**Visual:** This shifts the center of our "cloud" toward the uphill slope.

---

##### 3. Updating the Covariance Matrix $C$ (The Hard Part)

This is the core of CMA-ES. We need to update the matrix $C$ so that in the next generation, the random noise automatically shoots along the path of success.

###### Attempt A: The Naive Estimate (Slide 35)
$$C^{g+1}_{estimate} = \sum_{i=1}^{\mu} w_i (x_i - m)(x_i - m)^T$$

This is the standard statistical formula for calculating the covariance of a set of points.
*   $(x - m)(x - m)^T$ is the **Outer Product**. It creates a matrix representing the direction of *that specific step*.
*   **The Problem:** If we just use this, we throw away all the knowledge from previous generations. It’s too "jumpy" and unstable because we only have a few samples ($\mu$) every generation.

###### The Real Solution: Rank-$\mu$ Update (Slide 37)
To fix the "jumpiness," we use **Exponential Smoothing**. We keep the old matrix and blend in a little bit of the new data.

**The Math:**
$$C^{g+1} = \underbrace{(1 - c_\mu) C^g}_{\text{Keep old shape}} + \underbrace{c_\mu \sum w_i (\dots)(\dots)^T}_{\text{Add new info}}$$

*   **$c_\mu$ (Learning Rate):** A small number (between 0 and 1).
    *   If $c_\mu$ is 0.01, we keep 99% of the old shape and learn 1% from the new steps. This makes the shape change smooth and stable over time.
*   **Rank-$\mu$:** It is called this because the update adds a matrix of mathematical "Rank $\mu$" (constructed from $\mu$ vectors). It captures the **overall width/spread** of the successful population.

###### The Rank-One Update (Slide 38)
Sometimes, the "average" spread is too slow. We want to capture the specific **trajectory**.

**The Math:**
$$C^{g+1} = (1 - c_1)C^g + c_1 (x_1 - m)(x_1 - m)^T$$

*   Here, we update the matrix using **only the single best step** ($x_1 - m$).
*   This is called a **Rank-One** update.
*   **Why?** It is much more aggressive. It helps stretch the matrix quickly along a single leading direction.

**The Real CMA-ES (Slide 39):**
In the actual algorithm (which gets complex), we combine both:
1.  **Rank-$\mu$:** To learn the global width (preventing the cloud from collapsing).
2.  **Rank-One:** To learn the specific direction (elongating the cloud).

---

### Summary of the Math Flow

1.  **Generate** points using the current matrix $C$.
2.  **Calculate** the new center $m$ (Weighted average of winners).
3.  **Update $C$**:
    *   Take the old $C$.
    *   Multiply by roughly $(1 - \text{learning rate})$.
    *   Add the "shape" of the winning steps (Outer products).
    *   This stretches $C$ so it "remembers" where the good steps were.

So, mathematically, **Adaptation is just exponential smoothing applied to a covariance matrix.**

