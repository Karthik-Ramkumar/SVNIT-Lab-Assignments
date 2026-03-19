import random

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

n = 8
random.seed(987654)

def path_cost(p):
    s = 0
    for i in range(n-1):
        s += cost[p[i]][p[i+1]]
    s += cost[p[n-1]][p[0]]
    return s

def random_path():
    p = [0,1,2,3,4,5,6,7]
    random.shuffle(p)
    return p

def one_point(p1,p2):
    c = random.randint(1, n-1)
    child = p1[:c]
    for x in p2:
        if x not in child:
            child.append(x)
    return child

def two_point(p1,p2):
    a = random.randint(0, n-2)
    b = random.randint(a+1, n-1)

    child = [-1]*n

    for i in range(a,b):
        child[i] = p1[i]

    idx = 0
    for x in p2:
        if x not in child:
            while child[idx] != -1:
                idx += 1
            child[idx] = x

    return child

def mutate(child):
    while True:
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        if i != j:
            break
    child[i], child[j] = child[j], child[i]
    return child

def get_two_different_parents(pop):
    pop.sort(key=path_cost)

    p1 = pop[0]
    p2 = None

    for i in range(1, len(pop)):
        if pop[i] != p1:
            p2 = pop[i]
            break

    if p2 is None:
        while True:
            p2 = random_path()
            if p2 != p1:
                break

    return p1, p2

def genetic(crossover_type):
    pop = []
    nodes_explored = 0
    depth_explored = 0
    prev_best = -1
    convergence_gen = -1

    for i in range(20):
        pop.append(random_path())
        nodes_explored += 1

    for gen in range(50):
        p1, p2 = get_two_different_parents(pop)

        current_best = path_cost(p1)

        if current_best == prev_best and convergence_gen == -1:
            convergence_gen = gen
        prev_best = current_best

        print("Generation =", gen)
        print("Parent 1 =", p1, "Cost =", path_cost(p1))
        print("Parent 2 =", p2, "Cost =", path_cost(p2))

        new = []

        for i in range(20):
            while True:
                if crossover_type == 1:
                    child = one_point(p1, p2)
                else:
                    child = two_point(p1, p2)

                child = mutate(child)   # guarantees different offspring
                nodes_explored += 1

                if child != p1 and child != p2 and child not in new:
                    break

            new.append(child)

            if gen % 10 == 0:
                print("Offspring", i+1, "=", child, "Cost =", path_cost(child))

        print()

        pop = new
        depth_explored += 1

    pop.sort(key=path_cost)
    best = pop[0]

    print("crossover =", crossover_type)
    print("cost =", path_cost(best))
    print("path =", best)
    print("nodes explored =", nodes_explored)
    print("depth explored =", depth_explored)

    if convergence_gen == -1:
        print("convergence = not fully converged within 50 generations")
    else:
        print("convergence started at generation =", convergence_gen)
    print()

genetic(1)
genetic(2)