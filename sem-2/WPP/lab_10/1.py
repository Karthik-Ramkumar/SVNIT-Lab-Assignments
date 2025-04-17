def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n)
            board[row] = -1  # Backtrack
def print_solution(board, n):
    for i in range(n):
        row = ['.'] * n
        row[board[i]] = 'Q'
        print(" ".join(row))
    print("\n")

def eight_queens():
    n = 8
    board = [-1] * n
    solve_n_queens(board, 0, n)

eight_queens()
