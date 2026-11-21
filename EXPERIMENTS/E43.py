import numpy as np


class GridWorld:
    """4x4 grid: (0,0) start, (3,3) goal (+10), (1,1) and (2,2) traps (-5)."""

    def __init__(self):
        self.rows, self.cols = 4, 4
        self.goal = (3, 3)
        self.traps = {(1, 1), (2, 2)}
        self.state = (0, 0)

    def reset(self):
        self.state = (0, 0)
        return self.state

    def step(self, action: int):
        # 0: up, 1: down, 2: left, 3: right
        r, c = self.state
        if action == 0:
            r = max(0, r - 1)
        elif action == 1:
            r = min(self.rows - 1, r + 1)
        elif action == 2:
            c = max(0, c - 1)
        elif action == 3:
            c = min(self.cols - 1, c + 1)

        self.state = (r, c)
        if self.state == self.goal:
            return self.state, 10.0, True
        if self.state in self.traps:
            return self.state, -5.0, False
        return self.state, -0.1, False


def train_q_learning(episodes=1000, alpha=0.1, gamma=0.99, epsilon=0.2):
    env = GridWorld()
    q_table = np.zeros((env.rows, env.cols, 4))
    rng = np.random.default_rng(42)

    for _ in range(episodes):
        r, c = env.reset()
        done = False
        while not done:
            if rng.random() < epsilon:
                action = int(rng.integers(0, 4))
            else:
                action = int(np.argmax(q_table[r, c]))

            (nr, nc), reward, done = env.step(action)
            best_next = np.max(q_table[nr, nc])
            q_table[r, c, action] += alpha * (reward + gamma * best_next - q_table[r, c, action])
            r, c = nr, nc

    return env, q_table


def main():
    env, q_table = train_q_learning()
    state = env.reset()
    path = [state]
    action_names = {0: "UP", 1: "DOWN", 2: "LEFT", 3: "RIGHT"}
    actions_taken = []

    for _ in range(20):
        r, c = state
        action = int(np.argmax(q_table[r, c]))
        actions_taken.append(action_names[action])
        state, _, done = env.step(action)
        path.append(state)
        if done:
            break

    print("Learned path:", path)
    print("Actions:", actions_taken)


if __name__ == "__main__":
    main()