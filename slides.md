---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: 'text-center'
highlighter: shiki
lineNumbers: true
info: |
  ## The Gambler's Ruin Problem
  A Stochastic Analysis Presentation
drawings:
  persist: false
css: unocss
---

<script setup lang="ts">
import { onMounted } from 'vue'
import Chart from 'chart.js/auto'

// Initialize all charts when component is mounted
onMounted(() => {
  // Expected Bets Plot
  const expectedBetsCtx = document.getElementById('expectedBetsPlot') as HTMLCanvasElement
  if (expectedBetsCtx) {
    const N = 100
    const k = Array.from({length: N+1}, (_, i) => i)
    const Ek = k.map(x => x * (N - x))

    new Chart(expectedBetsCtx, {
      type: 'line',
      data: {
        labels: k,
        datasets: [{
          label: 'Expected Number of Bets',
          data: Ek,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    })
  }

  // Simulation Plot
  const simCtx = document.getElementById('simulationPlot') as HTMLCanvasElement
  if (simCtx) {
    const simData = Array.from({length: 100}, () =>
      Math.floor(Math.random() * 1000))

    new Chart(simCtx, {
      type: 'bar',
      data: {
        labels: Array.from({length: 10}, (_, i) => i * 100),
        datasets: [{
          label: 'Steps Distribution',
          data: simData,
          backgroundColor: 'rgba(54, 162, 235, 0.5)'
        }]
      }
    })
  }

  // Bias Effect Plot
  const biasCtx = document.getElementById('biasEffectPlot') as HTMLCanvasElement
  if (biasCtx) {
    const pValues = [0.45, 0.50, 0.55]
    const ruinProb = [0.9231, 0.8000, 0.5385]

    new Chart(biasCtx, {
      type: 'line',
      data: {
        labels: pValues,
        datasets: [{
          label: 'Probability of Ruin',
          data: ruinProb,
          borderColor: 'rgb(255, 99, 132)',
          tension: 0.1
        }]
      }
    })
  }

  // Wealth Evolution Plot
  const wealthCtx = document.getElementById('wealthEvolutionPlot') as HTMLCanvasElement
  if (wealthCtx) {
    const steps = Array.from({length: 50}, (_, i) => i)
    const wealth = steps.map(x => 10000 + Math.random() * 1000 - 500)

    new Chart(wealthCtx, {
      type: 'line',
      data: {
        labels: steps,
        datasets: [{
          label: 'Wealth Evolution',
          data: wealth,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      }
    })
  }

  // Outcome Distribution Plot
  const distCtx = document.getElementById('outcomeDistributionPlot') as HTMLCanvasElement
  if (distCtx) {
    const outcomes = ['Success', 'Ruin']
    const frequencies = [2011, 7989]

    new Chart(distCtx, {
      type: 'pie',
      data: {
        labels: outcomes,
        datasets: [{
          data: frequencies,
          backgroundColor: [
            'rgba(75, 192, 192, 0.5)',
            'rgba(255, 99, 132, 0.5)'
          ]
        }]
      }
    })
  }

  // Success probability by initial capital
  const successProbCtx = document.getElementById('successProbabilityPlot') as HTMLCanvasElement
  if (successProbCtx) {
    const initialCapital = Array.from({length: 11}, (_, i) => i)
    const successProbFair = initialCapital.map(i => i/10)
    const successProbFavorable = initialCapital.map(i => {
      const q_p = 2/3
      return (1 - Math.pow(q_p, i)) / (1 - Math.pow(q_p, 10))
    })
    const successProbUnfavorable = initialCapital.map(i => {
      const q_p = 1.2
      return (1 - Math.pow(q_p, i)) / (1 - Math.pow(q_p, 10))
    })

    new Chart(successProbCtx, {
      type: 'line',
      data: {
        labels: initialCapital,
        datasets: [
          {
            label: 'Fair Game (p=0.5)',
            data: successProbFair,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
          },
          {
            label: 'Favorable (p=0.6)',
            data: successProbFavorable,
            borderColor: 'rgb(54, 162, 235)',
            tension: 0.1
          },
          {
            label: 'Unfavorable (p=0.45)',
            data: successProbUnfavorable,
            borderColor: 'rgb(255, 99, 132)',
            tension: 0.1
          }
        ]
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Success Probability'
            }
          },
          x: {
            title: {
              display: true,
              text: 'Initial Capital'
            }
          }
        }
      }
    })
  }

  // Insurance risk model
  const insuranceCtx = document.getElementById('insuranceRiskPlot') as HTMLCanvasElement
  if (insuranceCtx) {
    const reserves = Array.from({length: 11}, (_, i) => i)
    const ruinProbabilities = [
      {
        label: 'p=0.55 (E(Δ)=0.1)',
        data: reserves.map(i => Math.pow(0.45/0.55, i)),
        borderColor: 'rgb(255, 99, 132)'
      },
      {
        label: 'p=0.6 (E(Δ)=0.2)',
        data: reserves.map(i => Math.pow(0.4/0.6, i)),
        borderColor: 'rgb(54, 162, 235)'
      },
      {
        label: 'p=0.65 (E(Δ)=0.3)',
        data: reserves.map(i => Math.pow(0.35/0.65, i)),
        borderColor: 'rgb(75, 192, 192)'
      }
    ]

    new Chart(insuranceCtx, {
      type: 'line',
      data: {
        labels: reserves,
        datasets: ruinProbabilities
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Probability of Eventual Ruin'
            }
          },
          x: {
            title: {
              display: true,
              text: 'Initial Reserve'
            }
          }
        }
      }
    })
  }
})
</script>

# The Gambler's Ruin Problem
## A Stochastic Analysis

A mathematical exploration of probability and risk

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">1/15</span>
</div>

---
layout: two-cols
---

# Introduction

The **Gambler's Ruin Problem** is a classic problem in probability theory that models:

- A gambler with initial capital
- Repeated betting on fair/biased games
- Two possible outcomes:
  - Reach target wealth
  - Lose everything

<div class="mt-4 text-sm">
This model captures fundamental principles of:

- Risk assessment
- Sequential decision-making under uncertainty
- Resource management with limited capital
</div>

::right::

<div class="ml-4 flex flex-col gap-4">
<img src="https://f.hellowork.com/edito/sites/5/2021/05/21279-768x432.jpg" alt="american-roulette">
<img src="https://i0.wp.com/www.fairlynerdy.com/wp-content/uploads/2016/03/Gamblers_Ruin_1.png?fit=719%2C467" alt="american-roulette">

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">2/15</span>
</div>

---

# Key Notations

<div class="grid grid-cols-2 gap-4">

<div class="p-4 bg-blue-50 rounded-lg">

## Basic Parameters
- **i**: Initial wealth (where $0 < i < N$)
- **N**: Target wealth
- **p**: Probability of winning
- **q**: Probability of losing (= 1 - p)
- **$X_n$**: Fortune after the $n$-th game

</div>

<div class="p-4 bg-green-50 rounded-lg">

## Probability Measures
- **$P_i$**: Probability of success starting with i
- **$E_i$**: Expected number of bets starting with i
- **$R_i$**: Probability of ruin starting with i
  - $R_i = 1 - P_i$

</div>

</div>

<div class="mt-4 p-4 bg-yellow-50 rounded-lg">

## Markov Chain Properties
- The sequence $\{X_n\}$ forms a Markov chain
- State space $S = \{0, 1, ..., N\}$
- States 0 and N are absorbing states
- Transition probabilities depend only on current state

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">3/15</span>
</div>

---

# Problem Statement

<div class="grid grid-cols-2 gap-4">

<div>

<v-clicks>

- Initial wealth: **i** dollars (where $0 < i < N$)
- Fixed bet amount of $1 each game
- Probability of winning: **p**
- Probability of losing: **q = 1 - p**
- Target wealth: **N**
- Games are independent of each other
- Play continues until either reaching N (success) or 0 (ruin)

</v-clicks>

<div class="mt-8">

## Objectives

<v-clicks>

1. Calculate probability of reaching target **$P_i$** before ruin
2. Determine probability of ruin **$R_i$**
3. Find expected number of bets **$E_i$**
4. Analyze effect of varying probabilities

</v-clicks>

</div>

</div>

<div>
  <img src="https://i0.wp.com/www.fairlynerdy.com/wp-content/uploads/2016/03/Gamblers_Ruin_1.png?fit=719%2C467"
   class="rounded-lg shadow-xl" />

   <div class="mt-4 p-4 bg-purple-50 rounded-lg text-sm">
     <strong>Real-world applications:</strong>
     <ul class="mt-2">
       <li>Financial markets and trading</li>
       <li>Insurance risk modeling</li>
       <li>Drug testing and clinical trials</li>
       <li>Population genetics</li>
     </ul>
   </div>
</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">4/15</span>
</div>

---
layout: center
---

# Transition Matrix

For a target fortune of $N = 4$, the transition matrix is:

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-4 bg-purple-50 rounded-lg">

## Matrix Representation

$$P =
\begin{pmatrix}
1 & 0 & 0 & 0 & 0 \\
q & 0 & p & 0 & 0 \\
0 & q & 0 & p & 0 \\
0 & 0 & q & 0 & p \\
0 & 0 & 0 & 0 & 1
\end{pmatrix}$$

<div class="mt-4 text-sm">
- Row/column 0: Ruin state (absorbing)
- Row/column N: Success state (absorbing)
- Rows 1 through N-1: Transient states
</div>

</div>

<div class="p-4 bg-blue-50 rounded-lg">

## Python Implementation

```python
import numpy as np

def transition_matrix(N, p):
    """
    Create transition matrix for gambler's ruin

    Parameters:
    N: Target fortune
    p: Probability of winning

    Returns:
    P: Transition matrix
    """
    q = 1 - p
    P = np.zeros((N+1, N+1))

    # Absorbing states
    P[0, 0] = 1
    P[N, N] = 1

    # Transient states
    for i in range(1, N):
        P[i, i-1] = q
        P[i, i+1] = p

    return P
```

</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">5/15</span>
</div>

---
layout: center
---

# Mathematical Formulation

Let **$P_i$** be the probability of reaching **N** starting with **i** dollars.

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-4 bg-purple-50 rounded-lg">

## Recurrence Relation

$$
P_i = p P_{i+1} + q P_{i-1}
$$

With boundary conditions:
$$
P_0 = 0, \quad P_N = 1
$$

<div class="mt-4 text-sm">
This is derived by conditioning on the outcome of the first game:
- With probability p, we win and move to state i+1
- With probability q, we lose and move to state i-1
</div>

</div>

<div class="p-4 bg-yellow-50 rounded-lg">

## Solution

For p ≠ q:
$$
P_i = \frac{1 - (q/p)^i}{1 - (q/p)^N}
$$

For fair game (p = q = 0.5):
$$
P_i = \frac{i}{N}
$$

<div class="mt-4 text-sm">
This shows that for a fair game, the success probability is simply proportional to initial capital.
</div>

</div>

</div>

<div class="mt-4 p-4 bg-green-50 rounded-lg">
<canvas id="successProbabilityPlot" width="600" height="300"></canvas>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">6/15</span>
</div>

---

# Expected Number of Bets

<div class="grid grid-cols-2 gap-4">

<div>

The expected number of plays ($E_i$) follows:

$$
E_i = 1 + p E_{i+1} + q E_{i-1}
$$

With boundary conditions:
$$
E_0 = E_N = 0
$$

For a fair game (p = 0.5):

$$
E_i = i(N - i)
$$

</div>

<div>
  <canvas id="expectedBetsPlot" width="400" height="300"></canvas>
</div>

</div>

<div class="mt-4 grid grid-cols-2 gap-4">
<div class="p-4 bg-red-50 rounded-lg">

## Interpretation
- Maximum at i = N/2
- Symmetric around N/2
- Quadratic growth
- Games starting near boundaries end more quickly

</div>
<div class="p-4 bg-blue-50 rounded-lg">

## Python Implementation
```python
def expected_bets(i, N, p=0.5):
    """Calculate expected number of bets"""
    if p == 0.5:  # Fair game
        return i * (N - i)
    else:
        q = 1 - p
        r = q / p
        if r == 1:  # Just in case of rounding
            return i * (N - i)
        else:
            num = i - N * (1 - r**i) / (1 - r**N)
            den = (p - q)
            return num / den
```

</div>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">7/15</span>
</div>

---
layout: two-cols
---

## Enhanced Simulation

```python {all}
import numpy as np
import matplotlib.pyplot as plt

def gamblers_ruin_simulation(
    initial_money, target, p, num_simulations=10000):

    ruin_count = 0
    success_count = 0
    total_steps = []
    final_states = []
    wealth_trajectories = []

    for _ in range(num_simulations):
        money = initial_money
        steps = 0
        trajectory = [money]

        while 0 < money < target:
            money += 1 if np.random.rand() < p else -1
            steps += 1
            trajectory.append(money)

        if money == 0:
            ruin_count += 1
        else:
            success_count += 1

        total_steps.append(steps)
        final_states.append(money)
        wealth_trajectories.append(trajectory)

    return {
        'ruin_prob': ruin_count / num_simulations,
        'success_prob': success_count / num_simulations,
        'avg_steps': np.mean(total_steps),
        'steps_dist': total_steps,
        'trajectories': wealth_trajectories
    }
```

::right::

<div class="ml-4">

## Calculating Theoretical Values

```python
def theoretical_success_prob(i, N, p):
    """Calculate theoretical success probability"""
    if p == 0.5:  # Fair game
        return i / N
    else:
        q = 1 - p
        r = q / p
        if r == 1:  # For numerical stability
            return i / N
        else:
            return (1 - r**i) / (1 - r**N)

def theoretical_ruin_prob(i, N, p):
    """Calculate theoretical ruin probability"""
    return 1 - theoretical_success_prob(i, N, p)

def infinite_game_success_prob(i, p):
    """Success probability with no upper bound"""
    if p <= 0.5:  # Unfair or fair game
        return 0
    else:
        q = 1 - p
        return 1 - (q/p)**i
```

## Simulation Results
<canvas id="simulationPlot" width="400" height="300"></canvas>

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">8/15</span>
</div>

---

# Illustrative Examples

<div class="grid grid-cols-2 gap-4">

<div class="p-4 bg-blue-50 rounded-lg">

## Example 1: Success Probability with Favorable Odds

**Problem**: John starts with $2, and has a 60% chance of winning each bet ($p = 0.6$). What is the probability that John reaches a fortune of $4 without going broke?

**Solution**:
- Initial fortune: $i = 2$
- Target: $N = 4$
- Win probability: $p = 0.6$, therefore $q = 0.4$
- $\frac{q}{p} = \frac{0.4}{0.6} = \frac{2}{3}$

Using the formula:
$$P_2 = \frac{1-(\frac{2}{3})^2}{1-(\frac{2}{3})^4} = \frac{1-\frac{4}{9}}{1-\frac{16}{81}} = \frac{\frac{5}{9}}{\frac{65}{81}} = \frac{5 \cdot 81}{9 \cdot 65} \approx 0.91$$

Therefore, John has approximately a 91% chance of reaching $4 without going broke.

</div>

<div class="p-4 bg-green-50 rounded-lg">

## Example 2: Stock Price Movement

**Problem**: Ellen bought a share of stock for $10, and it is believed that the stock price moves as a simple random walk with $p = 0.55$. What is the probability that Ellen's stock reaches $15 before falling to $5?

**Solution**:
- This is equivalent to a gambler starting with $i = 5$ aiming for $N = 10$
- $\frac{q}{p} = \frac{0.45}{0.55} \approx 0.82$

Using the formula:
$$P_5 = \frac{1-(0.82)^5}{1-(0.82)^{10}} \approx 0.73$$

Ellen has approximately a 73% chance that her stock will reach $15 before falling to $5.

</div>

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-4 bg-yellow-50 rounded-lg">

## Example 3: Infinite Game

**Problem**: With $p = 0.6$ and initial capital $i = 2$, what is the probability of never going broke (becoming infinitely rich)?

**Solution**:
For $p > 0.5$ as $N \to \infty$, the probability is:
$$P_i = 1-(\frac{q}{p})^i$$

With $i = 2$:
$$P_2 = 1-(\frac{0.4}{0.6})^2 = 1-\frac{4}{9} = \frac{5}{9} \approx 0.56$$

The gambler has approximately a 56% chance of never going broke.

</div>

<div class="p-4 bg-purple-50 rounded-lg">

## Example 4: Different Initial Capital

**Problem**: How does the probability of success change with different initial capitals when $p = 0.6$ and $N = 10$?

**Solution**:
Using our formula for each initial capital:

| Initial Capital | Success Probability |
|-----------------|---------------------|
| 1               | 0.65                |
| 2               | 0.81                |
| 5               | 0.97                |
| 8               | 0.99                |

This demonstrates the significant advantage of starting with higher capital.

</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">9/15</span>
</div>

---

# The Effect of Bias (p)

<div class="grid grid-cols-2 gap-4">

<div class="p-4 bg-blue-50 rounded-lg">

## Theoretical Impact

<table class="w-full">
  <thead class="bg-blue-100">
    <tr>
      <th class="p-2">p Value</th>
      <th class="p-2">Description</th>
      <th class="p-2">Long-term Behavior</th>
    </tr>
  </thead>
  <tbody>
    <tr class="bg-white">
      <td class="p-2">p < 0.5</td>
      <td class="p-2">Unfavorable</td>
      <td class="p-2">Ruin is certain if N = ∞</td>
    </tr>
    <tr class="bg-blue-50">
      <td class="p-2">p = 0.5</td>
      <td class="p-2">Fair</td>
      <td class="p-2">Ruin is certain if N = ∞</td>
    </tr>
    <tr class="bg-white">
      <td class="p-2">p > 0.5</td>
      <td class="p-2">Favorable</td>
      <td class="p-2">Positive probability of never going broke</td>
    </tr>
  </tbody>
</table>

<div class="mt-4 text-sm">
For infinite games (N = ∞):
- If p ≤ 0.5: Ruin is certain
- If p > 0.5: Probability of never going broke is 1-(q/p)^i
</div>

</div>

<div class="p-4 bg-green-50 rounded-lg">

## Simulation Results (i=20, N=100)

<table class="w-full">
  <thead class="bg-green-100">
    <tr>
      <th class="p-2">p Value</th>
      <th class="p-2">P(Ruin)</th>
      <th class="p-2">Avg Steps</th>
    </tr>
  </thead>
  <tbody>
    <tr class="bg-white">
      <td class="p-2">0.45</td>
      <td class="p-2">0.9231</td>
      <td class="p-2">156.3</td>
    </tr>
    <tr class="bg-green-50">
      <td class="p-2">0.50</td>
      <td class="p-2">0.8000</td>
      <td class="p-2">398.5</td>
    </tr>
    <tr class="bg-white">
      <td class="p-2">0.55</td>
      <td class="p-2">0.5385</td>
      <td class="p-2">687.2</td>
    </tr>
  </tbody>
</table>

<canvas id="biasEffectPlot" width="400" height="200" class="mt-4"></canvas>

</div>

</div>

<div class="mt-4 grid grid-cols-3 gap-4">
<div class="p-4 bg-red-50 rounded-lg">

## Key Insight 1
Small changes in p have dramatic effects on ruin probability.

</div>
<div class="p-4 bg-yellow-50 rounded-lg">

## Key Insight 2
Average game length increases significantly with favorable odds.

</div>
<div class="p-4 bg-purple-50 rounded-lg">

## Key Insight 3
Initial capital becomes more important as p decreases.

</div>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">10/15</span>
</div>

---
layout: center
---

# Maximum and Minimum Values

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-4 bg-purple-50 rounded-lg">

## Maximum Value Distribution (p < 0.5)

When p < 0.5, the random walk will eventually drift to -∞. The maximum value M reached before this happens has a geometric distribution:

$$P(M \geq a) = \left(\frac{p}{q}\right)^a$$

<div class="mt-4 text-sm">
- This gives the probability that a gambler with unfavorable odds will ever reach a certain high point
- Useful for analyzing "best case" scenarios in unfavorable conditions
</div>

</div>

<div class="p-4 bg-blue-50 rounded-lg">

## Minimum Value Distribution (p > 0.5)

When p > 0.5, the random walk will eventually drift to +∞. The minimum value m reached before this happens has a geometric distribution:

$$P(m \leq -b) = \left(\frac{q}{p}\right)^b$$

<div class="mt-4 text-sm">
- This gives the probability that a gambler with favorable odds will experience a certain drawdown
- Useful for risk management and setting appropriate reserves
</div>

</div>

</div>

<div class="mt-4 p-4 bg-green-50 rounded-lg">

## Python Implementation

```python
def max_value_distribution(a, p):
    """Probability of reaching at least value a when p < 0.5"""
    if p >= 0.5:
        return 1.0  # Will reach any value with probability 1
    q = 1 - p
    return (p/q)**a

def min_value_distribution(b, p):
    """Probability of reaching at most value -b when p > 0.5"""
    if p <= 0.5:
        return 1.0  # Will reach any value with probability 1
    q = 1 - p
    return (q/p)**b
```

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">11/15</span>
</div>

---

# Application: Insurance Risk Modeling

<div class="grid grid-cols-2 gap-4">

<div>

## Insurance Risk Model

- Insurance company earns $1 per day from premiums
- May suffer a claim of $1 with probability q = 1-p
- Initial reserve of i ≥ 1
- Probability of eventual ruin follows our formula:
  $$R_i = \left(\frac{q}{p}\right)^i \text{ for } p > q$$

<div class="mt-4 p-4 bg-blue-50 rounded-lg">

## Key Insight

Insurance company must maintain:
- p > 0.5 for sustainable operations
- Expected net income per day (E(Δ) = p - q) must be positive
- Higher initial reserves dramatically reduce ruin probability

</div>

</div>

<div>
  <canvas id="insuranceRiskPlot" width="400" height="300"></canvas>

  <div class="mt-4 p-4 bg-green-50 rounded-lg">

  ## Mathematical Model

  Each day can be modeled as:
  - Income: +1 with certainty
  - Claim: -2 with probability q
  - Net: +1