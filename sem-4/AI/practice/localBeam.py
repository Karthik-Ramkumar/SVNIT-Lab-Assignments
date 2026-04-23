# k = number of best states kept at each step

def local_beam_search(matrix, start, goal, k):
    n = len(matrix)
    beam = [(start, [start], 0)]   # (current_city, path, total_cost)

    while beam:
        all_successors = []

        for current, path, total_cost in beam:
            if current == goal:
                print("Path:", [cities[i] for i in path])
                print("Cost:", total_cost)
                return

            for i in range(n):
                if i not in path and matrix[current][i] != 0:
                    new_path = path + [i]
                    new_cost = total_cost + matrix[current][i]
                    all_successors.append((i, new_path, new_cost))

        if not all_successors:
            break

        all_successors.sort()
        beam = all_successors[:k]

    print("Goal not reachable!")


cities = ['A','B','C','D','E','F','G','H']

cost = [
    [0,10,15,20,25,30,35,40],
    [12,0,35,15,20,25,30,45],
    [25,30,0,10,40,20,15,35],
    [18,25,12,0,15,30,20,10],
    [22,18,28,20,0,15,25,30],
    [35,22,18,28,12,0,40,20],
    [30,35,22,18,28,32,0,15],
    [40,28,35,22,18,25,12,0]
]

start_city = 0   # A
goal_city = 7    # H
k = 4

local_beam_search(cost, start_city, goal_city, k)