import numpy as np


class TinyMLP:
    """2 -> 4 -> 1 neural network with tanh hidden activation and sigmoid output."""

    def __init__(self, input_dim=2, hidden_dim=4, output_dim=1):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.genome_size = (
            input_dim * hidden_dim + hidden_dim + hidden_dim * output_dim + output_dim
        )

    def forward(self, X: np.ndarray, weights: np.ndarray) -> np.ndarray:
        idx = 0
        w1_size = self.input_dim * self.hidden_dim
        W1 = weights[idx : idx + w1_size].reshape(self.input_dim, self.hidden_dim)
        idx += w1_size

        b1 = weights[idx : idx + self.hidden_dim]
        idx += self.hidden_dim

        w2_size = self.hidden_dim * self.output_dim
        W2 = weights[idx : idx + w2_size].reshape(self.hidden_dim, self.output_dim)
        idx += w2_size

        b2 = weights[idx : idx + self.output_dim]

        h = np.tanh(X @ W1 + b1)
        out = 1.0 / (1.0 + np.exp(-(h @ W2 + b2)))
        return out


def evolve_xor_network(generations=200, pop_size=80, mutation_std=0.25):
    X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
    y = np.array([[0.0], [1.0], [1.0], [0.0]])

    rng = np.random.default_rng(42)
    net = TinyMLP(input_dim=2, hidden_dim=4, output_dim=1)
    population = rng.normal(0.0, 1.0, size=(pop_size, net.genome_size))

    def fitness(genome):
        preds = net.forward(X, genome)
        mse = np.mean((y - preds) ** 2)
        return -float(mse)

    for gen in range(1, generations + 1):
        scores = np.array([fitness(ind) for ind in population])
        best_idx = int(np.argmax(scores))

        if gen == 1 or gen % 40 == 0 or gen == generations:
            best_preds = net.forward(X, population[best_idx]).flatten()
            print(f"Gen {gen:3d} | MSE: {-scores[best_idx]:.5f} | Preds: {np.round(best_preds, 3)}")

        # Elitism + tournament selection
        elite_count = 4
        elite_indices = np.argsort(scores)[-elite_count:]
        next_pop = [population[i].copy() for i in elite_indices]

        while len(next_pop) < pop_size:
            i1, i2 = rng.integers(0, pop_size, size=2)
            p1 = population[i1 if scores[i1] > scores[i2] else i2]

            j1, j2 = rng.integers(0, pop_size, size=2)
            p2 = population[j1 if scores[j1] > scores[j2] else j2]

            mask = rng.random(net.genome_size) < 0.5
            child = np.where(mask, p1, p2)
            child += rng.normal(0.0, mutation_std, size=net.genome_size)
            next_pop.append(child)

        population = np.array(next_pop)

    best_genome = population[int(np.argmax([fitness(ind) for ind in population]))]
    print("\nFinal XOR predictions vs targets:")
    for inp, target, pred in zip(X, y.flatten(), net.forward(X, best_genome).flatten()):
        print(f"  Input={inp.astype(int).tolist()} -> Target={int(target)}, Pred={pred:.4f}")


if __name__ == "__main__":
    evolve_xor_network()