# Iterative Deepening Search using adjacency matrix

def dls(adj_matrix, start, goal, limit):
    n = len(adj_matrix)
    visited = [False] * n
    stack = [(start, 0)]

    while stack:
        node, depth = stack.pop()

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            if node == goal:
                return True

            if depth < limit:
                for i in range(n - 1, -1, -1):
                    if adj_matrix[node][i] == 1 and not visited[i]:
                        stack.append((i, depth + 1))

    return False


def ids(adj_matrix, start, goal, max_limit):
    for limit in range(max_limit + 1):
        print("\nDepth Limit", limit, ":", end=" ")
        found = dls(adj_matrix, start, goal, limit)

        if found:
            print("\nGoal reached at depth", limit)
            return

    print("\nGoal not found!")


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
max_depth = 3

ids(adj_matrix, start_node, goal_node, max_depth)