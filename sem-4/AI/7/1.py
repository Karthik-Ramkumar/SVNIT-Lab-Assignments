import random

def random_board():
    return [random.randint(0, 7) for _ in range(8)]

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
            return current_h, steps, ("Solved" if current_h == 0 else "Fail")

        current = best[:]
        current_h = best_h
        steps += 1

print(f"{'Run':<5} | {'Initial H':<10} | {'Final H':<8} | {'Steps':<6} | {'Status'}")
print("-" * 50)

fail_count = 0
success_count = 0

for i in range(50):
    board = random_board()
    initial_h = heuristic(board)
    final_h, steps, status = steepest_ascent(board)

    if status == "Fail":
        fail_count += 1
    else:
        success_count += 1

    print(f"{i+1:<5} | {initial_h:<10} | {final_h:<8} | {steps:<6} | {status}")

print("\n--- Statistics ---")
print(f"Total Successes: {success_count}")
print(f"Total Fails (Local Minima): {fail_count}")
print(f"Success Rate: {(success_count/50)*100}%")