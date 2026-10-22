from collections import deque
def water_jug_bfs(jug1_cap, jug2_cap, target):
    queue = deque([(0, 0, [])])
    visited = set()
    while queue:
        curr_j1, curr_j2, path = queue.popleft()
        if curr_j1 == target or curr_j2 == target:
            path.append((curr_j1, curr_j2))
            return path
        if (curr_j1, curr_j2) in visited:
            continue
        visited.add((curr_j1, curr_j2))
        current_path = path + [(curr_j1, curr_j2)]
        possible_moves = [
            (jug1_cap, curr_j2),
            (curr_j1, jug2_cap),
            (0, curr_j2),
            (curr_j1, 0),
            (curr_j1 - min(curr_j1, jug2_cap - curr_j2), curr_j2 + min(curr_j1, jug2_cap - curr_j2)),
            (curr_j1 + min(curr_j2, jug1_cap - curr_j1), curr_j2 - min(curr_j2, jug1_cap - curr_j1))
        ]
        for move in possible_moves:
            if move not in visited:
                queue.append((move[0], move[1], current_path))
    return None
if __name__ == "__main__":
    JUG_1_CAPACITY = 4
    JUG_2_CAPACITY = 3
    TARGET_AMOUNT = 2
    print(f"Solving Water Jug Problem for Jug 1: {JUG_1_CAPACITY}L, Jug 2: {JUG_2_CAPACITY}L, Target: {TARGET_AMOUNT}L\n")
    solution = water_jug_bfs(JUG_1_CAPACITY, JUG_2_CAPACITY, TARGET_AMOUNT)
    if solution:
        print("Solution found! Step-by-step states (Jug1, Jug2):")
        for step_num, state in enumerate(solution):
            print(f"Step {step_num}: {state}")
    else:
        print("No solution is possible with these jug capacities.")