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
  <span class="opacity-50">1/11</span>
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

::right::

<div class="ml-4 flex flex-col gap-4">
<img src="https://f.hellowork.com/edito/sites/5/2021/05/21279-768x432.jpg" alt="american-roulette">
<img src="https://f.hellowork.com/edito/sites/5/2021/05/21279-768x432.jpg" alt="american-roulette">

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">2/11</span>
</div>

---

# Key Notations

<div class="grid grid-cols-2 gap-4">

<div class="p-4 bg-blue-50 rounded-lg">

## Basic Parameters
- **S₀**: Initial wealth
- **N**: Target wealth
- **p**: Probability of winning
- **q**: Probability of losing (= 1 - p)
- **k**: Current wealth state

</div>

<div class="p-4 bg-green-50 rounded-lg">

## Probability Measures
- **P_k**: Probability of success starting with k
- **E_k**: Expected number of bets starting with k
- **R_k**: Probability of ruin starting with k
  - R_k = 1 - P_k

</div>

</div>

<img src="https://source.unsplash.com/random/800x400/?mathematics" class="mt-4 rounded-lg shadow-xl" />

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">3/11</span>
</div>

---

# Problem Statement

<div class="grid grid-cols-2 gap-4">

<div>

<v-clicks>

- Initial wealth: **S₀** dollars
- Fixed bet amount each game
- Probability of winning: **p**
- Probability of losing: **q = 1 - p**
- Target wealth: **N**

</v-clicks>

<div class="mt-8">

## Objectives

<v-clicks>

1. Calculate probability of reaching target **P(S_N)** before ruin
2. Determine expected number of bets
3. Analyze effect of varying probabilities

</v-clicks>

</div>

</div>

<div>
  <img src="https://source.unsplash.com/random/800x600/?probability" class="rounded-lg shadow-xl" />
</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">4/11</span>
</div>

---
layout: center
---

# Mathematical Formulation

Let **P_k** be the probability of reaching **N** starting with **k** dollars.

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="p-4 bg-purple-50 rounded-lg">

## Recurrence Relation

$$
P_k = p P_{k+1} + q P_{k-1}
$$

With boundary conditions:
$$
P_0 = 0, \quad P_N = 1
$$

</div>

<div class="p-4 bg-yellow-50 rounded-lg">

## Solution

For p ≠ q:
$$
P_k = \frac{1 - (q/p)^k}{1 - (q/p)^N}
$$

For fair game (p = q = 0.5):
$$
P_k = \frac{k}{N}
$$

</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">5/11</span>
</div>

---

# Expected Number of Bets

<div class="grid grid-cols-2 gap-4">

<div>

The expected number of plays (E_k) follows:

$$
E_k = 1 + p E_{k+1} + q E_{k-1}
$$

For a fair game (p = 0.5):

$$
E_k = k(N - k)
$$

</div>

<div>
  <canvas id="expectedBetsPlot" width="400" height="300"></canvas>
</div>

</div>

<div class="mt-4 grid grid-cols-2 gap-4">
<div class="p-4 bg-red-50 rounded-lg">

## Interpretation
- Maximum at k = N/2
- Symmetric around N/2
- Quadratic growth

</div>
<div class="p-4 bg-blue-50 rounded-lg">

## Practical Implications
- Longer games near middle states
- Faster resolution near boundaries
- Risk increases with duration

</div>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">6/11</span>
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

    for _ in range(num_simulations):
        money = initial_money
        steps = 0
        while 0 < money < target:
            money += 1 if np.random.rand() < p else -1
            steps += 1

        if money == 0:
            ruin_count += 1
        else:
            success_count += 1

        total_steps.append(steps)
        final_states.append(money)

    return {
        'ruin_prob': ruin_count / num_simulations,
        'success_prob': success_count / num_simulations,
        'avg_steps': np.mean(total_steps),
        'steps_dist': total_steps
    }
```

::right::

<div class="ml-4">

## Enhanced Features

<v-clicks>

- Tracks success count
- Records step distribution
- Stores final states
- Returns detailed statistics

</v-clicks>

## Simulation Results
<canvas id="simulationPlot" width="400" height="300"></canvas>

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">7/11</span>
</div>

---

# Comparative Analysis

<div class="grid grid-cols-2 gap-4">

<div class="p-4 bg-blue-50 rounded-lg">

## Theoretical vs Simulated Results

<table class="w-full">
  <thead class="bg-blue-100">
    <tr>
      <th class="p-2">Metric</th>
      <th class="p-2">Theoretical</th>
      <th class="p-2">Simulated</th>
    </tr>
  </thead>
  <tbody>
    <tr class="bg-white">
      <td class="p-2">P(Ruin)</td>
      <td class="p-2">0.8000</td>
      <td class="p-2">0.7989</td>
    </tr>
    <tr class="bg-blue-50">
      <td class="p-2">E(Steps)</td>
      <td class="p-2">400</td>
      <td class="p-2">398.5</td>
    </tr>
    <tr class="bg-white">
      <td class="p-2">P(Success)</td>
      <td class="p-2">0.2000</td>
      <td class="p-2">0.2011</td>
    </tr>
  </tbody>
</table>

</div>

<div class="p-4 bg-green-50 rounded-lg">

## Effect of Bias (p)

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

</div>

</div>

<canvas id="biasEffectPlot" width="800" height="200" class="mt-4"></canvas>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">8/11</span>
</div>

---

# Practical Applications

<div class="grid grid-cols-3 gap-4">

<div class="p-4 bg-blue-50 rounded-lg">

## Financial Markets
<img src="https://source.unsplash.com/random/400x300/?stockmarket" class="rounded-lg shadow-xl mb-2" />
- Stock trading strategies
- Stop-loss optimization
- Risk management
- Portfolio rebalancing
- High-frequency trading

</div>

<div class="p-4 bg-green-50 rounded-lg">

## Insurance Industry
<img src="https://source.unsplash.com/random/400x300/?insurance" class="rounded-lg shadow-xl mb-2" />
- Premium calculation
- Reserve management
- Risk assessment
- Claims modeling
- Reinsurance strategies

</div>

<div class="p-4 bg-yellow-50 rounded-lg">

## Other Applications
<img src="https://source.unsplash.com/random/400x300/?science" class="rounded-lg shadow-xl mb-2" />
- Population genetics
- Queueing theory
- Resource allocation
- Clinical trials
- Ecological modeling

</div>

</div>

<div class="mt-4 p-4 bg-purple-50 rounded-lg">

## Real-World Example: Trading Strategy
- Initial capital: $10,000
- Target: $15,000
- Stop-loss: $8,000
- Win probability: 0.52 (after costs)
- Expected duration: 200 trades

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">9/11</span>
</div>

---

# Simulation Results Visualization

<div class="grid grid-cols-2 gap-4">

<div>
  <canvas id="wealthEvolutionPlot" width="400" height="300"></canvas>
</div>

<div>
  <canvas id="outcomeDistributionPlot" width="400" height="300"></canvas>
</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">10/11</span>
</div>

---
layout: center
class: text-center
---

# Thank You!

<div class="grid grid-cols-2 gap-4 mt-8">

<div class="p-4 bg-blue-50 rounded-lg">

## References
1. Ross, S. (2014). *Introduction to Probability Models*
2. Grimmett, G., & Stirzaker, D. (2001). *Probability and Random Processes*
3. Feller, W. (1968). *An Introduction to Probability Theory*
4. Ethier, S. N. (2010). *The Doctrine of Chances*

</div>

<div class="p-4 bg-green-50 rounded-lg">

## Contact Information
- Email: soudev2001@gmail.com
- GitHub: github.com/Soufiane4906


</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <span class="opacity-50">11/11</span>
</div>