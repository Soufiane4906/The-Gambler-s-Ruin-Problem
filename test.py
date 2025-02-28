import numpy as np
import matplotlib.pyplot as plt

def gamblers_ruin_simulation(initial_money, target, p, num_simulations=10000):
    """
    Simule le problème de la ruine du joueur à l'aide d'une approche Monte Carlo.

    Paramètres:
    - initial_money: Capital initial du joueur.
    - target: Objectif de richesse à atteindre.
    - p: Probabilité de gagner un pari.
    - num_simulations: Nombre de simulations à effectuer.

    Retourne:
    - ruin_probability: Probabilité estimée de ruine.
    - avg_steps: Nombre moyen d'étapes avant la ruine ou le succès.
    """
    ruin_count = 0
    total_steps = []

    for _ in range(num_simulations):
        money = initial_money
        steps = 0

        while 0 < money < target:
            money += 1 if np.random.rand() < p else -1
            steps += 1

        if money == 0:
            ruin_count += 1
        total_steps.append(steps)

    ruin_probability = ruin_count / num_simulations
    avg_steps = np.mean(total_steps)

    return ruin_probability, avg_steps

# Paramètres d'exemple
initial_money = 10
target = 50
p = 0.3

ruin_prob, avg_steps = gamblers_ruin_simulation(initial_money, target, p)
print(f"Estimated Probability of Ruin: {ruin_prob}")
print(f"Average Steps Until Ruin or Success: {avg_steps}")

# Visualisation des trajectoires individuelles de la fortune du joueur
def plot_gamblers_paths(initial_money, target, p, num_paths=5):
    plt.figure(figsize=(10, 6))

    for _ in range(num_paths):
        money = initial_money
        history = [money]

        while 0 < money < target:
            money += 1 if np.random.rand() < p else -1
            history.append(money)

        plt.plot(history)

    plt.xlabel("Nombre de paris")
    plt.ylabel("Capital du joueur")
    plt.title("Évolution de la fortune du joueur dans le temps")
    plt.show()

# Affichage des trajectoires aléatoires du joueur
plot_gamblers_paths(initial_money, target, p)
