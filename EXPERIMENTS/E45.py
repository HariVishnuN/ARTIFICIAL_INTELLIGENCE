from collections import defaultdict
import random


class MarkovChain:
    def __init__(self):
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.probabilities = {}

    def fit(self, sequences):
        for seq in sequences:
            for current_state, next_state in zip(seq[:-1], seq[1:]):
                self.transitions[current_state][next_state] += 1

        for state, next_counts in self.transitions.items():
            total = sum(next_counts.values())
            self.probabilities[state] = {nxt: cnt / total for nxt, cnt in next_counts.items()}

    def predict_next(self, current_state, rng: random.Random):
        if current_state not in self.probabilities:
            return None
        next_map = self.probabilities[current_state]
        states = list(next_map.keys())
        weights = list(next_map.values())
        return rng.choices(states, weights=weights, k=1)[0]

    def generate_sequence(self, start_state, length=8, seed=42):
        rng = random.Random(seed)
        seq = [start_state]
        for _ in range(length - 1):
            nxt = self.predict_next(seq[-1], rng)
            if nxt is None:
                break
            seq.append(nxt)
        return seq


def main():
    training_sequences = [
        ["sunny", "sunny", "rainy", "cloudy", "sunny"],
        ["sunny", "cloudy", "rainy", "rainy", "cloudy"],
        ["cloudy", "sunny", "sunny", "cloudy", "rainy"],
        ["rainy", "cloudy", "sunny", "sunny", "sunny"],
    ]

    model = MarkovChain()
    model.fit(training_sequences)

    print("Transition probabilities from 'sunny':", model.probabilities.get("sunny", {}))
    predicted_seq = model.generate_sequence(start_state="sunny", length=8)
    print("Predicted sequence:", " -> ".join(predicted_seq))


if __name__ == "__main__":
    main()