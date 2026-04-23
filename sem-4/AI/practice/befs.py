# Best First Search using adjacency matrix + heuristic values

def best_first_search(matrix, h, start, goal):
    n = len(matrix)
    visited = [False] * n
    open_list = []

    open_list.append(start)

    print("Best First Search Traversal:", end=" ")

    while open_list:
        open_list.sort(key=lambda x: h[x])
        node = open_list.pop(0)

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            if node == goal:
                print("\nGoal reached!")
                return

            for i in range(n):
                if matrix[node][i] == 1 and not visited[i]:
                    open_list.append(i)


# Example
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

heuristic = [5, 4, 3, 2, 0]

start_node = 0
goal_node = 4

best_first_search(adj_matrix, heuristic, start_node, goal_node)