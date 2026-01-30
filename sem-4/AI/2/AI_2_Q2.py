start = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

goal = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    # Fixed order: up, down, left, right
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(r) for r in new_state))
    return neighbors

# DFS using stack
stack = [(start, 0)]   # (state, depth)
visited = set()
states_explored = 0

while stack:
    current, depth = stack.pop()
    if current in visited:
        continue

    visited.add(current)
    states_explored += 1

    if current == goal:
        goal_depth = depth
        break

    for neighbor in get_neighbors(current):
        if neighbor not in visited:
            stack.append((neighbor, depth + 1))

print("DFS states explored:", states_explored)
print("Goal depth (DFS):", goal_depth)
