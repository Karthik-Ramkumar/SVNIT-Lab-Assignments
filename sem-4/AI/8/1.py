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

n = 8 # number of cities
seed = 1234567

def rand():
    global seed
    seed = (seed*1103515245 + 12345) % 2147483648
    return seed

def randn(x): # gives back a value between 0-> x-1 for choosing random city
    return rand() % x

def path_cost(p):
    s = 0
    for i in range(n-1):
        s += cost[p[i]][p[i+1]]
    s += cost[p[n-1]][p[0]]
    return s

def random_path():
    p = [0,1,2,3,4,5,6,7]
    for i in range(n):
        j = randn(n)
        p[i],p[j] = p[j],p[i]
    return p

def neighbors(p):
    arr = []
    for i in range(n):
        for j in range(i+1,n):
            q = p[:]
            q[i],q[j] = q[j],q[i]
            arr.append(q)
    return arr

def beam_search(k,steps):
    beam = []
    for i in range(k):
        beam.append(random_path())

    best = beam[0]
    best_cost = path_cost(best)

    for t in range(steps):
        cand = []
        for b in beam:
            nb = neighbors(b)
            for x in nb:
                cand.append(x)
        for i in range(len(cand)):

            for j in range(i+1,len(cand)):
                if path_cost(cand[j]) < path_cost(cand[i]):
                    cand[i],cand[j] = cand[j],cand[i]

        beam = cand[:k]

        c = path_cost(beam[0])
        if c < best_cost:
            best = beam[0]
            best_cost = c

    print("k =",k)
    print("cost =",best_cost)
    print("path =",best)
    print()

beam_search(3,20)
beam_search(5,20)
beam_search(10,20)