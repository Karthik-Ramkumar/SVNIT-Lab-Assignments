# Map Coloring using Backtracking

def is_safe(node, color, colors, graph):
    for i in range(len(graph)):
        if graph[node][i] == 1 and colors[i] == color:
            return False
    return True

def map_coloring(graph, m, colors, node):
    n = len(graph)

    if node == n:
        return True

    for color in range(1, m + 1):
        if is_safe(node, color, colors, graph):
            colors[node] = color

            if map_coloring(graph, m, colors, node + 1):
                return True

            colors[node] = 0

    return False


# Example
graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

m = 3
colors = [0] * len(graph)

if map_coloring(graph, m, colors, 0):
    print("Color Assignment:", colors)
else:
    print("No solution")