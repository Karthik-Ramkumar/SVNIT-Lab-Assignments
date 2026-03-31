# First Choice, Random Restart, Simulated Annealing
# No libraries used

seed = 1234567
def rand():
    global seed
    seed = (seed * 1103515245 + 12345) % 2147483648
    return seed

def rand8():
    return rand() % 8

def random_board():
    board = []
    for i in range(8):
        board.append(rand8())
    return board

def heuristic(board):
    h = 0
    for i in range(8):
        for j in range(i+1, 8):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                h += 1
    return h

def first_choice(board):
    current = board[:]
    current_h = heuristic(current)
    steps = 0

    while True:
        improved = False
        for col in range(8):
            original = current[col]
            for row in range(8):
                if row != original:
                    current[col] = row
                    h = heuristic(current)
                    if h < current_h:
                        current_h = h
                        improved = True
                        steps += 1
                        break
            if improved:
                break
            current[col] = original

        if not improved:
            return current_h, steps, ("Solved" if current_h == 0 else "Fail")

# Random Restart Hill Climbing 
def steepest(board):
    current = board[:]
    current_h = heuristic(current)
    steps = 0

    while True:
        best = current[:]
        best_h = current_h

        for col in range(8):
            original = current[col]
            for row in range(8):
                if row != original:
                    current[col] = row
                    h = heuristic(current)
                    if h < best_h:
                        best_h = h
                        best = current[:]
            current[col] = original

        if best_h >= current_h:
            return current_h, steps, ("Solved" if current_h == 0 else "Fail")

        current = best[:]
        current_h = best_h
        steps += 1

def random_restart():
    restarts = 0
    total_steps = 0
    while True:
        board = random_board()
        final_h, steps, status = steepest(board)
        total_steps += steps
        if final_h == 0:
            return restarts, total_steps
        restarts += 1

# Simulated Annealing 

def simulated_annealing(board):
    current = board[:]
    current_h = heuristic(current)
    steps = 0
    T = 100.0
    cooling = 0.95

    while T > 0.1 and current_h > 0:
        col = rand8()
        row = rand8()
        old_row = current[col]

        current[col] = row
        new_h = heuristic(current)

        delta = new_h - current_h

        if delta < 0:
            current_h = new_h
        else:
            # accept with probability e^(-delta/T)
            # approximate using simple threshold
            prob = 1.0
            temp = T
            count = 0
            while count < delta:
                prob = prob * 0.5
                count += 1
            if (rand() % 1000)/1000.0 < prob:
                current_h = new_h
            else:
                current[col] = old_row

        T = T * cooling
        steps += 1

    return current_h, steps, ("Solved" if current_h == 0 else "Fail")

# Experiment

print("Method Comparison (50 runs each)")
print("----------------------------------")

# First Choice
fc_success = 0
for i in range(50):
    board = random_board()
    final_h, steps, status = first_choice(board)
    if status == "Solved":
        fc_success += 1
print("First Choice Success:", fc_success, "/50")

# Random Restart
rr_success = 0
for i in range(50):
    restarts, steps = random_restart()
    rr_success += 1
print("Random Restart Success:", rr_success, "/50")

# Simulated Annealing
sa_success = 0
for i in range(50):
    board = random_board()
    final_h, steps, status = simulated_annealing(board)
    if status == "Solved":
        sa_success += 1
print("Simulated Annealing Success:", sa_success, "/50")

print("\n===== FINAL COMPARISON (50 Runs Each) =====\n")

# ---------------- First Choice ----------------
fc_success = 0
fc_total_steps = 0

for i in range(50):
    board = random_board()
    final_h, steps, status = first_choice(board)
    fc_total_steps += steps
    if status == "Solved":
        fc_success += 1

print("First Choice Hill Climbing")
print("Success :", fc_success, "/50")
print("Failure :", 50 - fc_success)
print("Success Rate :", (fc_success/50)*100, "%")
print("Average Steps :", fc_total_steps/50)
print("------------------------------------------")


# ---------------- Random Restart ----------------
rr_total_restarts = 0
rr_total_steps = 0

for i in range(50):
    restarts, steps = random_restart()
    rr_total_restarts += restarts
    rr_total_steps += steps

print("Random Restart Hill Climbing")
print("Success : 50 / 50 (Always succeeds)")
print("Average Restarts :", rr_total_restarts/50)
print("Average Steps :", rr_total_steps/50)
print("------------------------------------------")


# ---------------- Simulated Annealing ----------------
sa_success = 0
sa_total_steps = 0

for i in range(50):
    board = random_board()
    final_h, steps, status = simulated_annealing(board)
    sa_total_steps += steps
    if status == "Solved":
        sa_success += 1

print("Simulated Annealing")
print("Success :", sa_success, "/50")
print("Failure :", 50 - sa_success)
print("Success Rate :", (sa_success/50)*100, "%")
print("Average Steps :", sa_total_steps/50)
print("------------------------------------------")