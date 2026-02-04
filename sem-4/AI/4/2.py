# 0 = free , 1 = wall
ROWS = 8
COLS = 12

grid = [
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,1,1,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,1,0,1],
[1,1,1,1,1,1,1,1,0,1,0,1],
[1,0,0,0,0,0,0,1,0,0,0,1],
[1,0,1,1,1,1,0,0,0,1,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1]
]

goal_r = 3
goal_c = 10

entry_r = 5
entry_c = 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def absval(x):
    if x < 0:
        return -x
    return x

def heuristic(r,c):
    return absval(goal_r-r) + absval(goal_c-c)

def goal_test(r,c):
    if r==goal_r and c==goal_c:
        return True
    return False

# Node = [r,c,parent_index,g,f]

frontier = []
reached = []

# reached table (matrix, no dictionaries)
for i in range(ROWS):
    row=[]
    for j in range(COLS):
        row.append(-1)
    reached.append(row)

def expand(node_index, nodes):
    children = []

    r = nodes[node_index][0]
    c = nodes[node_index][1]
    g = nodes[node_index][3]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr>=0 and nr<ROWS and nc>=0 and nc<COLS:
            if grid[nr][nc]==0:
                ng = g + 1
                nf = ng + heuristic(nr,nc)
                child = [nr,nc,node_index,ng,nf]
                children.append(child)

    return children


nodes = []

start_f = heuristic(entry_r,entry_c)
start = [entry_r,entry_c,-1,0,start_f]

nodes.append(start)
frontier.append(0)
reached[entry_r][entry_c] = 0

solution_index = -1

while len(frontier) != 0:

    # pop lowest f (priority queue using list)
    best_i = 0
    for i in range(1,len(frontier)):
        if nodes[frontier[i]][4] < nodes[frontier[best_i]][4]:
            best_i = i

    node_index = frontier[best_i]
    frontier.pop(best_i)

    r = nodes[node_index][0]
    c = nodes[node_index][1]

    if goal_test(r,c):
        solution_index = node_index
        break

    children = expand(node_index, nodes)

    for child in children:
        s_r = child[0]
        s_c = child[1]

        add_flag = False

        if reached[s_r][s_c] == -1:
            add_flag = True
        else:
            old_index = reached[s_r][s_c]
            if child[3] < nodes[old_index][3]:
                add_flag = True

        if add_flag:
            nodes.append(child)
            new_index = len(nodes)-1
            reached[s_r][s_c] = new_index
            frontier.append(new_index)


if solution_index == -1:
    print("No path found")
else:
    path = []
    cur = solution_index
    while cur != -1:
        path.append([nodes[cur][0],nodes[cur][1]])
        cur = nodes[cur][2]

    i = len(path)-1
    while i>=0:
        print(path[i][0], path[i][1])
        i -= 1
