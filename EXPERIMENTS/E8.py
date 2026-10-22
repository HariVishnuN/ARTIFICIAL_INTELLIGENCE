def dfs(graph, node, visited=None, traversal=None):
    if visited is None: visited, traversal = set(), []
    if node not in visited:
        visited.add(node)
        traversal.append(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited, traversal)
    return traversal
if __name__ == "__main__":
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors of {node} separated by space (or leave blank): ").split()
        graph[node] = neighbors
    start_node = input("Enter start node: ")
    print("DFS Traversal:", dfs(graph, start_node))