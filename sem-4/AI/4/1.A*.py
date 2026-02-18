

cities = [
    "Chicago","Detroit","Cleveland","Indianapolis","Columbus",
    "Pittsburgh","Buffalo","Syracuse","NewYork","Philadelphia",
    "Baltimore","Boston","Providence","Portland"
]

n = len(cities)
INF = 9999999

graph = [
# Chi Det Cle Ind Col Pit Buf Syr NY  Phi Bal Bos Pro Por
[  0,283,345,182,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # chi
[283,  0,169,  0,  0,  0,256,  0,  0,  0,  0,  0,  0,  0], # det
[345,169,  0,  0,144,134,189,  0,  0,  0,  0,  0,  0,  0], # cle
[182,  0,  0,  0,176,  0,  0,  0,  0,  0,  0,  0,  0,  0], # ind
[  0,  0,144,176,  0,185,  0,  0,  0,  0,  0,  0,  0,  0], # col
[  0,  0,134,  0,185,  0,215,  0,  0,305,247,  0,  0,  0], # pit
[  0,256,189,  0,  0,215,  0,150,  0,  0,  0,  0,  0,  0], # buf
[  0,  0,  0,  0,  0,  0,150,  0,254,253,  0,312,  0,  0], # syr
[  0,  0,  0,  0,  0,  0,  0,254,  0, 97,  0,  0,181,  0], # ny
[  0,  0,  0,  0,  0,305,  0,253, 97,  0,101,215,  0,  0], # phi
[  0,  0,  0,  0,  0,247,  0,  0,  0,101,  0,  0,  0,  0], # bal
[  0,  0,  0,  0,  0,  0,  0,312,  0,215,  0,  0, 50,107], # bos
[  0,  0,  0,  0,  0,  0,  0,  0,181,  0,  0, 50,  0,  0], # pro
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,107,  0,  0]  # por
]


h = {
"Chicago":860,"Detroit":610,"Cleveland":550,"Indianapolis":780,"Columbus":640,"Pittsburgh":470,
"Buffalo":400,"Syracuse":260,"NewYork":215,"Philadelphia":270,"Baltimore":360,"Boston":0,
"Providence":50,"Portland":107
}

class Node:
    def __init__(self,state,parent=None,cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

def expand(node):
    children=[]
    i=cities.index(node.state)
    for j in range(n):
        if graph[i][j]!=0:
            city=cities[j]
            cost=node.cost+graph[i][j]
            children.append(Node(city,node,cost))
    return children

def solution(node):
    path=[]
    while node:
        path.append(node.state)
        node=node.parent
    return path[::-1]

def BEST_FIRST_SEARCH(start,goal):
    frontier=[]
    reached={}
    startNode=Node(start,None,0)
    frontier.append(startNode)
    reached[start]=startNode

    nodes_explored=0

    while frontier:
        # f(n) = g(n) + h(n)
        frontier.sort(key=lambda x: x.cost + h[x.state])
        node=frontier.pop(0)
        nodes_explored+=1

        if node.state==goal:
            return solution(node),nodes_explored

        for child in expand(node):
            s=child.state
            if s not in reached or child.cost<reached[s].cost:
                reached[s]=child
                frontier.append(child)

    return None,nodes_explored

path,explored=BEST_FIRST_SEARCH("Syracuse","Chicago")

print("Path:",path)
print("Nodes explored:",explored)

