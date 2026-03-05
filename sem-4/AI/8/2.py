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
seed = 987654

def rand():
    global seed
    seed = (seed*1103515245 + 12345) % 2147483648
    return seed

def randn(x):
    return rand()%x

def path_cost(p):
    s=0
    for i in range(n-1):
        s+=cost[p[i]][p[i+1]]
    s+=cost[p[n-1]][p[0]]
    return s

def random_path():
    p=[0,1,2,3,4,5,6,7]
    for i in range(n):
        j=randn(n)
        p[i],p[j]=p[j],p[i]
    return p

def one_point(p1,p2):
    c=randn(n)
    child=p1[:c]
    for x in p2:
        if x not in child:
            child.append(x)
    return child

def two_point(p1,p2):
    a=randn(n)
    b=randn(n)
    if a>b:
        a,b=b,a

    child=[-1]*n # initialize child with -1

    for i in range(a,b):
        child[i]=p1[i]

    idx=0
    for x in p2:
        if x not in child:
            while child[idx]!=-1:
                idx+=1
            child[idx]=x

    return child

def genetic(crossover_type):
    pop=[]
    for i in range(20):
        pop.append(random_path())

    for gen in range(50):

        for i in range(len(pop)):
            for j in range(i+1,len(pop)):
                if path_cost(pop[j])<path_cost(pop[i]):
                    pop[i],pop[j]=pop[j],pop[i]

        p1=pop[0]
        p2=pop[1]

        new=[]

        for i in range(20):
            if crossover_type==1:
                child=one_point(p1,p2)
            else:
                child=two_point(p1,p2)

            new.append(child)

        pop=new

    best=pop[0]
    print("crossover =",crossover_type)
    print("cost =",path_cost(best))
    print("path =",best)
    print()

genetic(1)
genetic(2)