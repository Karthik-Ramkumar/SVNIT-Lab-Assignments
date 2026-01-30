# Start and Goal states (0 = blank)
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

# Find position of blank (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate next states
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

# BFS
queue = [start]
visited = set()
visited.add(start)

states_explored = 0

while queue:
    current = queue.pop(0)
    states_explored += 1

    if current == goal:
        break

    for neighbor in get_neighbors(current):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print("States explored before reaching goal:", states_explored)
