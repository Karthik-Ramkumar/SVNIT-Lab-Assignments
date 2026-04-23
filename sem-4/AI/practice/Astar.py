# A* Search using adjacency matrix + heuristic values
# (Assuming every edge cost = 1)

def a_star_search(adj_matrix, heuristic, start, goal):
    n = len(adj_matrix)
    visited = [False] * n
    g_cost = [999] * n
    open_list = []

    g_cost[start] = 0
    open_list.append(start)

    print("A* Traversal:", end=" ")

    while open_list:
        open_list.sort(key=lambda x: g_cost[x] + heuristic[x])
        node = open_list.pop(0)

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            if node == goal:
                print("\nGoal reached!")
                return

            for i in range(n):
                if adj_matrix[node][i] == 1 and not visited[i]:
                    new_cost = g_cost[node] + 1

                    if new_cost < g_cost[i]:
                        g_cost[i] = new_cost

                    open_list.append(i)

    print("\nGoal not reachable!")


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

a_star_search(adj_matrix, heuristic, start_node, goal_node)