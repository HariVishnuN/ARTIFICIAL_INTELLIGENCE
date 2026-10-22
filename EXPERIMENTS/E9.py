import itertools
def traveling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_path, min_cost = None, float('inf')
    for perm in itertools.permutations(nodes):
        path = [start] + list(perm) + [start]
        cost = sum(graph[path[i]].get(path[i+1], float('inf')) for i in range(len(path)-1))
        if cost < min_cost:
            min_cost, min_path = cost, path
    return min_path, min_cost
if __name__ == "__main__":
    graph = {}
    nodes = input("Enter all node names separated by space: ").split()
    for u in nodes:
        graph[u] = {}
        for v in nodes:
            if u == v:
                graph[u][v] = 0
            else:
                graph[u][v] = int(input(f"Enter distance from {u} to {v}: "))
    start_node = input("Enter start node: ")
    path, cost = traveling_salesman(graph, start_node)
    print(f"Optimal TSP Path: {path} with Cost: {cost}")