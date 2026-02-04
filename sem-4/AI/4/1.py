# BEST FIRST SEARCH USING MATRIX (CITY GRAPH)

# ---------------- CITIES ----------------
cities = [
    "Chicago","Detroit","Cleveland","Indianapolis","Columbus",
    "Pittsburgh","Buffalo","Syracuse","NewYork","Philadelphia",
    "Baltimore","Boston","Providence","Portland"
]

n = len(cities)
INF = 9999999

# ---------------- ADJACENCY MATRIX ----------------
# 0 means no direct road
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

#  heuristic(to Chicago) 
h = {
"Chicago":0,"Detroit":283,"Cleveland":345,"Indianapolis":182,"Columbus":320,"Pittsburgh":460,
"Buffalo":540,"Syracuse":690,"NewYork":790,"Philadelphia":760,"Baltimore":700,"Boston":980,"Providence":1030,
"Portland":1090
}
class Node:
    def __init__(self,state,parent=None,cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

def expand(node): #generates all children (successor nodes) of current city
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

    while frontier: # frontier keeps all the cities that are generated but not yet explored
        frontier.sort(key=lambda x:h[x.state]) # for each node in x sort with heuristic value of that node's city
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

# ---------------- RUN ----------------
path,explored=BEST_FIRST_SEARCH("Boston","Chicago")

print("Path:",path)
print("Nodes explored:",explored)
