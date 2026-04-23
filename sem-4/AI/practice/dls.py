# Depth Limited Search (limit = 3) using adjacency matrix

def dls(adj_matrix, start, goal, limit):
    n = len(adj_matrix)
    visited = [False] * n
    stack = [(start, 0)]   # (node, depth)

    print("DLS Traversal:", end=" ")

    while stack:
        node, depth = stack.pop()

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            if node == goal:
                print("\nGoal reached!")
                return

            if depth < limit:
                for i in range(n - 1, -1, -1):
                    if adj_matrix[node][i] == 1 and not visited[i]:
                        stack.append((i, depth + 1))

    print("\nGoal not found within depth limit!")


# Example
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]

start_node = 0
goal_node = 4
limit = 3

dls(adj_matrix, start_node, goal_node, limit)