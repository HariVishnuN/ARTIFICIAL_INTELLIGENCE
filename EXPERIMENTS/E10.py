import heapq
def a_star(graph, heuristics, start, goal):
    open_list = [(heuristics[start], 0, start, [start])]
    closed_set = set()
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current == goal: return path, g
        if current in closed_set: continue
        closed_set.add(current)
        for neighbor, weight in graph.get(current, {}).items():
            if neighbor not in closed_set:
                new_g = g + weight
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')
if __name__ == "__main__":
    graph, heuristics = {}, {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node name: ")
        heuristics[node] = int(input(f"Enter heuristic value for {node}: "))
        graph[node] = {}
        edges = input(f"Enter neighbors and weights for {node} as 'Name:Weight' (e.g., B:2 C:3) or leave blank: ").split()
        for edge in edges:
            n_name, n_weight = edge.split(':')
            graph[node][n_name] = int(n_weight)
    start_node = input("Enter start node: ")
    goal_node = input("Enter goal node: ")
    path, cost = a_star(graph, heuristics, start_node, goal_node)
    print(f"A* Path: {path} with Total Cost: {cost}")