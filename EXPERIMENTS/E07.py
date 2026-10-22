from collections import deque
def bfs(graph, start):
    visited, queue, traversal = set([start]), deque([start]), []
    while queue:
        node = queue.popleft()
        traversal.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal
if __name__ == "__main__":
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors of {node} separated by space (or leave blank): ").split()
        graph[node] = neighbors
    start_node = input("Enter start node: ")
    print("BFS Traversal:", bfs(graph, start_node))