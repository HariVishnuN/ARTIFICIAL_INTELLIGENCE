def reflex_vacuum_agent(location, status_a, status_b):
    cost = 0
    print(f"Initial: Location={location}, A={'Dirty' if status_a else 'Clean'}, B={'Dirty' if status_b else 'Clean'}")
    if location == 'A':
        if status_a == 1:
            print("Room A is Dirty -> Action: SUCK")
            status_a, cost = 0, cost + 1
        if status_b == 1:
            print("Room B is Dirty -> Action: RIGHT")
            location, cost = 'B', cost + 1
            print("Room B is Dirty -> Action: SUCK")
            status_b, cost = 0, cost + 1
    else:
        if status_b == 1:
            print("Room B is Dirty -> Action: SUCK")
            status_b, cost = 0, cost + 1
        if status_a == 1:
            print("Room A is Dirty -> Action: LEFT")
            location, cost = 'A', cost + 1
            print("Room A is Dirty -> Action: SUCK")
            status_a, cost = 0, cost + 1
    print(f"Final: Both rooms clean. Total Cost: {cost}\n")
if __name__ == "__main__":
    print("Test Case 1: Start at A, Both Dirty")
    reflex_vacuum_agent('A', 1, 1)
    print("Test Case 2: Start at B, Only A is Dirty")
    reflex_vacuum_agent('B', 1, 0)