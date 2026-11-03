def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors.get(neighbor) == color: return False
    return True
def map_coloring(node, graph, m, colors, nodes):
    if node == len(nodes): return True
    current = nodes[node]
    for c in range(1, m + 1):
        if is_safe(current, c, graph, colors):
            colors[current] = c
            if map_coloring(node + 1, graph, m, colors, nodes): return True
            colors[current] = 0
    return False
if __name__ == "__main__":
    nodes = input("Enter regions separated by space: ").split()
    graph = {n: [] for n in nodes}
    edges = int(input("Enter number of adjacent pairs (edges): "))
    for _ in range(edges):
        u, v = input("Enter adjacent regions (e.g., A B): ").split()
        graph[u].append(v)
        graph[v].append(u)
    m = int(input("Enter maximum number of colors: "))
    colors = {n: 0 for n in nodes}
    if map_coloring(0, graph, m, colors, nodes):
        print("Solution Colors:", colors)
    else:
        print("No solution exists.")