# DFS using adjacency matrix

def dfs(adj_matrix, start):
    n = len(adj_matrix)
    visited = [False] * n
    stack = [start]

    print("DFS Traversal:", end=" ")

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            for i in range(n - 1, -1, -1):
                if adj_matrix[node][i] == 1 and not visited[i]:
                    stack.append(i)


# Example
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

start_node = 0
dfs(adj_matrix, start_node)
print("\n")