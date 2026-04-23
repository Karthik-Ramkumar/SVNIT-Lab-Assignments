# Uniform Cost Search using cost matrix

def uniform_cost_search(cost, start, goal):
    n = len(cost)
    visited = [False] * n
    open_list = [(0, start)]   # (total_cost, node)

    print("UCS Traversal:", end=" ")

    while open_list:
        open_list.sort()
        current_cost, node = open_list.pop(0)

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            if node == goal:
                print("\nGoal reached with cost =", current_cost)
                return

            for i in range(n):
                if cost[node][i] != 0 and not visited[i]:
                    open_list.append((current_cost + cost[node][i], i))

    print("\nGoal not reachable!")


# Example
cost = [
    [0,10,15,20,25],
    [10,0,35,25,17],
    [15,35,0,30,28],
    [20,25,30,0,12],
    [25,17,28,12,0]
]

start_node = 0
goal_node = 4

uniform_cost_search(cost, start_node, goal_node)