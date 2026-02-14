# State format:
# [girls_left, boys_left, boat_side]
# boat_side = 0 (left), 1 (right)
# [girls_moved, boys_moved]
RULES = [
    [1,0],
    [2,0],
    [0,1],
    [0,2],
    [1,1]
]

STATE_STACK = [[0,0,0] for _ in range(100)]
DEPTH_STACK = [0]*100
VISITED = [[-1,-1,-1] for _ in range(200)] # depth of each stack, -1  means it is not used
VISITED_COUNT = 0 # to avoid loopign

EXPLORED_DLS = 0
EXPLORED_IDS = 0

def valid(state):
    gl = state[0]
    bl = state[1]
    boat = state[2]
    gr = 3 - gl
    br = 3 - bl

    if gl < 0 or bl < 0 or gl > 3 or bl > 3: # reject invalid counts
        return 0
    if gl > 0 and bl > gl: # girls not outnumbered
        return 0
    if gr > 0 and br > gr:
        return 0

    return 1

def visited(state):
    global VISITED_COUNT
    i = 0
    while i < VISITED_COUNT:
        if VISITED[i][0]==state[0] and VISITED[i][1]==state[1] and VISITED[i][2]==state[2]:
            return 1
        i += 1
    return 0

def add_visited(state):
    global VISITED_COUNT
    VISITED[VISITED_COUNT][0]=state[0]
    VISITED[VISITED_COUNT][1]=state[1]
    VISITED[VISITED_COUNT][2]=state[2]
    VISITED_COUNT+=1

def goal(state):
    if state[0]==0 and state[1]==0 and state[2]==1:
        return 1
    return 0

def move(state, rule):
    new = [state[0],state[1],state[2]] #copy current state

    if state[2]==0:   # boat is on the left
        new[0] = state[0] - rule[0]
        new[1] = state[1] - rule[1]
        new[2] = 1 # send people right
    else:         # boat is on the right
        new[0] = state[0] + rule[0]
        new[1] = state[1] + rule[1]
        new[2] = 0 # fetch people back left with boat

    return new # return new state after applying rule to current state

def print_path(top):
    i=0
    while i<=top:
        print(STATE_STACK[i][0],STATE_STACK[i][1],STATE_STACK[i][2])
        i+=1

def DLS(limit):
    global VISITED_COUNT,EXPLORED_DLS
    VISITED_COUNT=0
    EXPLORED_DLS=0

    start=[3,3,0]
    STATE_STACK[0]=start
    DEPTH_STACK[0]=0
    top=0

    add_visited(start)

    while top>=0:

        current=STATE_STACK[top]
        depth=DEPTH_STACK[top]
        EXPLORED_DLS+=1

        if goal(current)==1:
            print("DLS SOLUTION:")
            print_path(top)
            return 1

        if depth==limit:
            top-=1
            continue

        i=0
        expanded=0
        while i<5:
            child=move(current,RULES[i])

            if valid(child)==1 and visited(child)==0:
                top+=1
                STATE_STACK[top]=child
                DEPTH_STACK[top]=depth+1
                add_visited(child)
                expanded=1
                break
            i+=1

        if expanded==0:
            top-=1

    return 0

def IDS():
    global VISITED_COUNT,EXPLORED_IDS
    EXPLORED_IDS=0

    depth=0
    while depth<=20:
        VISITED_COUNT=0

        start=[3,3,0]
        STATE_STACK[0]=start
        DEPTH_STACK[0]=0
        top=0
        add_visited(start)

        while top>=0:

            current=STATE_STACK[top]
            d=DEPTH_STACK[top]
            EXPLORED_IDS+=1

            if goal(current)==1:
                print("IDS SOLUTION:")
                print_path(top)
                return

            if d==depth:
                top-=1
                continue

            i=0
            expanded=0
            while i<5:
                child=move(current,RULES[i])

                if valid(child)==1 and visited(child)==0:
                    top+=1
                    STATE_STACK[top]=child
                    DEPTH_STACK[top]=d+1
                    add_visited(child)
                    expanded=1
                    break
                i+=1

            if expanded==0:
                top-=1

        depth+=1

print("Depth Limited Search limit=3")
DLS(3)
print("\nIterative Deepening Search")
IDS()


print("DLS explored:",EXPLORED_DLS)
print("IDS explored:",EXPLORED_IDS)