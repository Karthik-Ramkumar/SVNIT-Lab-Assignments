maze = [
    [2, 0, 0, 0, 1],
    [0, 1, 0, 0, 3],
    [0, 3, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [3, 0, 0, 0, 3]
]

rows = 5
cols = 5

# L U R D
actions = [(-1,0),(1,0),(0,-1),(0,1)]

# finding start
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 2:
            start = (i,j)

# finding all rewards
rewards = []
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 3:
            rewards.append((i,j))

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])   #mahanttan distance

def astar(start, goal):

    open_list = [(start, 0)]   #(state, goal) #nodes generated but not yet explored
    parent = {}
    closed = []

    while open_list:

        # choosing node with min( f = g + h)
        best_index = 0
        best_next_choice = open_list[0][1] + heuristic(open_list[0][0], goal)

        for i in range(len(open_list)):
            state, g = open_list[i]
            f = g + heuristic(state, goal)
            if f < best_next_choice:
                best_next_choice = f
                best_index = i

        state, g = open_list.pop(best_index)

        if state == goal:
            path = []
            while state in parent:
                path.append(state)
                state = parent[state]
            path.append(start)
            path.reverse() # path is constructed in reverse order cause of stack, so we reverse it to get the correct order
            return path

        closed.append(state)

        # expanding current node and handling neighbours
        for move in actions:
            nx = state[0] + move[0]
            ny = state[1] + move[1]
            new_state = (nx,ny) #generating all 4 neighbours

            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] != 1 and new_state not in closed: #checking if valid move and not already explored

                    new_g = g + 1 #new cost
                    found = False

                    for i in range(len(open_list)): #checking if this new neighbour is there in list 
                        if open_list[i][0] == new_state:
                            found = True
                            if new_g < open_list[i][1]: # if already discovered do this and update if cost is smaller
                                open_list[i] = (new_state, new_g)
                                parent[new_state] = state
                            break

                    if not found:
                        open_list.append((new_state, new_g))
                        parent[new_state] = state

    return []

current = start
visited_tiles = []

while rewards:
# here i am choosing goal state by heuristic also
    nearest = rewards[0]
    min_h = heuristic(current, nearest)

    for r in rewards:
        h = heuristic(current, r)
        if h < min_h:
            min_h = h
            nearest = r

    path = astar(current, nearest)

    for p in path:
        if p not in visited_tiles:
            visited_tiles.append(p)

    current = nearest
    rewards.remove(nearest)

print("Visited tiles:")
for v in visited_tiles:
    print(v)
