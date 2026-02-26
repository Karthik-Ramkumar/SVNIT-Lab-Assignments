# Board representation:
# index = column (0–7)
# value = row (0–7)

def random_board():
    board = []
seed = 54321

def random_board():
    global seed
    board = []
    for i in range(8):
        seed = (seed * 1103515245 + 12345) % 2147483648
        board.append(seed % 8)
    return board

def heuristic(board):
    h = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

def steepest_ascent(board):
    steps = 0
    current = board[:]
    current_h = heuristic(current)

    while True:
        best = current[:]
        best_h = current_h

        for col in range(8):
            original_row = current[col]
            for row in range(8):
                if row != original_row:
                    current[col] = row
                    h = heuristic(current)
                    if h < best_h:
                        best_h = h
                        best = current[:]
            current[col] = original_row

        if best_h >= current_h:
            return current_h, best_h, steps, ("Solved" if current_h == 0 else "Fail")

        current = best[:]
        current_h = best_h
        steps += 1


# Run 50 random boards
print("Run | Initial H | Final H | Steps | Status")
print("---------------------------------------------")

fail_count = 0

for i in range(50):
    board = random_board()
    initial_h = heuristic(board)
    init, final, steps, status = steepest_ascent(board)

    if status == "Fail":
        fail_count += 1

    print(i+1, "   ", initial_h, "        ", final, "       ", steps, "    ", status)

print("\nTotal Fails (Local Minima found):", fail_count)