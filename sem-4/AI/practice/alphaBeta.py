# Alpha-Beta Pruning for Tic-Tac-Toe

def print_board(board):
    for row in board:
        print(row)
    print()

def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 10
            elif board[i][0] == 'O':
                return -10

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == 'X':
                return 10
            elif board[0][j] == 'O':
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    return 0

def alphabeta(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, alphabeta(board, depth + 1, False, alpha, beta))
                    board[i][j] = '_'

                    alpha = max(alpha, best)

                    if beta <= alpha:
                        break

        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, alphabeta(board, depth + 1, True, alpha, beta))
                    board[i][j] = '_'

                    beta = min(beta, best)

                    if beta <= alpha:
                        break

        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_val = alphabeta(board, 0, False, -1000, 1000)
                board[i][j] = '_'

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move


# Example
board = [
    ['X', 'O', 'X'],
    ['O', '_', '_'],
    ['_', '_', 'O']
]

print("Current Board:")
print_board(board)

best_move = find_best_move(board)
print("Best Move for X:", best_move)