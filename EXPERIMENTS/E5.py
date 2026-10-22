from collections import deque
def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3: return False
    if (m > 0 and m < c) or (3 - m > 0 and 3 - m < 3 - c): return False
    return True
def solve_missionaries_cannibals():
    queue = deque([((3, 3, 1), [])])
    visited = set([(3, 3, 1)])
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    while queue:
        (m, c, b), path = queue.popleft()
        if (m, c, b) == (0, 0, 0): return path + [(0, 0, 0)]
        for dm, dc in moves:
            nm, nc, nb = (m - dm, c - dc, 0) if b == 1 else (m + dm, c + dc, 1)
            if is_valid(nm, nc) and (nm, nc, nb) not in visited:
                visited.add((nm, nc, nb))
                queue.append(((nm, nc, nb), path + [(m, c, b)]))
    return None
if __name__ == "__main__":
    print("Missionaries and Cannibals (Left Bank State)")
    solution = solve_missionaries_cannibals()
    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step}: Missionaries={state[0]}, Cannibals={state[1]}, Boat={'Left' if state[2]==1 else 'Right'}")
    else:
        print("No solution found.")