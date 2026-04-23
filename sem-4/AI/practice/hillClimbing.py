# Hill Climbing Variants (using city cost matrix)
# Goal: reach goal city with minimum path cost

import random
import math

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

def get_neighbors(current, path):
    neighbors = []
    for i in range(len(cost)):
        if i not in path and cost[current][i] != 0:
            neighbors.append(i)
    return neighbors

def hill_climbing(start, goal):
    current = start
    path = [current]
    total_cost = 0

    while current != goal:
        neighbors = get_neighbors(current, path)

        if not neighbors:
            break

        best = neighbors[0]
        best_cost = cost[current][best]

        for n in neighbors:
            if cost[current][n] < best_cost:
                best = n
                best_cost = cost[current][n]

        current = best
        path.append(current)
        total_cost += best_cost

    print("Normal Hill Climbing:")
    print("Path:", [cities[i] for i in path])
    print("Cost:", total_cost)
    print()

def stochastic_hill_climbing(start, goal):
    current = start
    path = [current]
    total_cost = 0

    while current != goal:
        neighbors = get_neighbors(current, path)

        if not neighbors:
            break

        better = []
        for n in neighbors:
            if cost[current][n] < 999:
                better.append(n)

        if not better:
            break

        next_node = random.choice(better)
        total_cost += cost[current][next_node]
        current = next_node
        path.append(current)

    print("Stochastic Hill Climbing:")
    print("Path:", [cities[i] for i in path])
    print("Cost:", total_cost)
    print()

def steepest_ascent_hill_climbing(start, goal):
    current = start
    path = [current]
    total_cost = 0

    while current != goal:
        neighbors = get_neighbors(current, path)

        if not neighbors:
            break

        best = neighbors[0]
        best_cost = cost[current][best]

        for n in neighbors:
            if cost[current][n] < best_cost:
                best = n
                best_cost = cost[current][n]

        current = best
        path.append(current)
        total_cost += best_cost

    print("Steepest Ascent Hill Climbing:")
    print("Path:", [cities[i] for i in path])
    print("Cost:", total_cost)
    print()

def random_restart_hill_climbing(goal, restarts):
    best_path = []
    best_cost = 9999

    for _ in range(restarts):
        start = random.randint(0, len(cost) - 1)
        current = start
        path = [current]
        total_cost = 0

        while current != goal:
            neighbors = get_neighbors(current, path)

            if not neighbors:
                break

            best = neighbors[0]
            best_step_cost = cost[current][best]

            for n in neighbors:
                if cost[current][n] < best_step_cost:
                    best = n
                    best_step_cost = cost[current][n]

            current = best
            path.append(current)
            total_cost += best_step_cost

        if current == goal and total_cost < best_cost:
            best_cost = total_cost
            best_path = path[:]

    print("Random Restart Hill Climbing:")
    if best_path:
        print("Path:", [cities[i] for i in best_path])
        print("Cost:", best_cost)
    else:
        print("Goal not reached")
    print()

def simulated_annealing(start, goal, temperature, cooling):
    current = start
    path = [current]
    total_cost = 0

    while temperature > 1 and current != goal:
        neighbors = get_neighbors(current, path)

        if not neighbors:
            break

        next_node = random.choice(neighbors)

        current_cost = 0
        next_cost = cost[current][next_node]

        diff = next_cost - current_cost

        if diff < 0 or random.random() < math.exp(-diff / temperature):
            current = next_node
            path.append(current)
            total_cost += next_cost

        temperature = temperature * cooling

    print("Simulated Annealing:")
    print("Path:", [cities[i] for i in path])
    print("Cost:", total_cost)
    print()


# Example
start_city = 0   # A
goal_city = 7    # H

hill_climbing(start_city, goal_city)
stochastic_hill_climbing(start_city, goal_city)
steepest_ascent_hill_climbing(start_city, goal_city)
random_restart_hill_climbing(goal_city, 5)
simulated_annealing(start_city, goal_city, 100, 0.9)