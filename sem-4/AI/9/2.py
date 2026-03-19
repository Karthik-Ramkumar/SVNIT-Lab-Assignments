import time

player = None

#  minimax performance
minimax_nodes_explored = 0
minimax_max_depth_reached = 0

#  a-b performacne 
alphabeta_nodes_explored = 0
alphabeta_max_depth_reached = 0
pruned_branches = 0


class TicTacToe:
    def TO_MOVE(self, state):
        x_count = 0
        o_count = 0

        for cell in state:
            if cell == 'X':
                x_count += 1
            elif cell == 'O':
                o_count += 1

        if x_count == o_count:
            return 'X'
        else:
            return 'O'

    def ACTIONS(self, state):
        actions = []
        for i in range(9):
            if state[i] == ' ':
                actions.append(i)
        return actions

    def RESULT(self, state, action):
        new_state = state[:]
        new_state[action] = self.TO_MOVE(state)
        return new_state

    def IS_TERMINAL(self, state):
        if self.winner(state) is not None:
            return True

        for cell in state:
            if cell == ' ':
                return False

        return True

    def UTILITY(self, state, player_symbol):
        winner = self.winner(state)

        if winner == player_symbol:
            return 1
        elif winner is None:
            return 0
        else:
            return -1

    def winner(self, state):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for w in wins:
            if state[w[0]] != ' ' and state[w[0]] == state[w[1]] and state[w[1]] == state[w[2]]:
                return state[w[0]]

        return None


# MINIMAX (for comparison)

def MINIMAX_SEARCH(game, state):
    global player
    player = game.TO_MOVE(state)
    value, move = MAX_VALUE_MINIMAX(game, state, 0)
    return move


def MAX_VALUE_MINIMAX(game, state, depth):
    global minimax_nodes_explored, minimax_max_depth_reached, player

    minimax_nodes_explored += 1
    if depth > minimax_max_depth_reached:
        minimax_max_depth_reached = depth

    if game.IS_TERMINAL(state):
        return game.UTILITY(state, player), None

    v = -999999
    move = None

    for a in game.ACTIONS(state):
        v2, a2 = MIN_VALUE_MINIMAX(game, game.RESULT(state, a), depth + 1)

        if v2 > v:
            v = v2
            move = a

    return v, move


def MIN_VALUE_MINIMAX(game, state, depth):
    global minimax_nodes_explored, minimax_max_depth_reached, player

    minimax_nodes_explored += 1
    if depth > minimax_max_depth_reached:
        minimax_max_depth_reached = depth

    if game.IS_TERMINAL(state):
        return game.UTILITY(state, player), None

    v = 999999
    move = None

    for a in game.ACTIONS(state):
        v2, a2 = MAX_VALUE_MINIMAX(game, game.RESULT(state, a), depth + 1)

        if v2 < v:
            v = v2
            move = a

    return v, move


# ALPHA-BETA PRUNING

def ALPHA_BETA_SEARCH(game, state):
    global player
    player = game.TO_MOVE(state)
    value, move = MAX_VALUE_AB(game, state, -999999, 999999, 0)
    return move


def MAX_VALUE_AB(game, state, alpha, beta, depth):
    global alphabeta_nodes_explored, alphabeta_max_depth_reached, pruned_branches, player

    alphabeta_nodes_explored += 1
    if depth > alphabeta_max_depth_reached:
        alphabeta_max_depth_reached = depth

    if game.IS_TERMINAL(state):
        return game.UTILITY(state, player), None

    v = -999999
    move = None

    actions = game.ACTIONS(state)

    for i in range(len(actions)):
        a = actions[i]

        v2, a2 = MIN_VALUE_AB(game, game.RESULT(state, a), alpha, beta, depth + 1)

        if v2 > v:
            v = v2
            move = a

        if v >= beta:
            pruned_branches += (len(actions) - i - 1)
            return v, move

        if v > alpha:
            alpha = v

    return v, move


def MIN_VALUE_AB(game, state, alpha, beta, depth):
    global alphabeta_nodes_explored, alphabeta_max_depth_reached, pruned_branches, player

    alphabeta_nodes_explored += 1
    if depth > alphabeta_max_depth_reached:
        alphabeta_max_depth_reached = depth

    if game.IS_TERMINAL(state):
        return game.UTILITY(state, player), None

    v = 999999
    move = None

    actions = game.ACTIONS(state)

    for i in range(len(actions)):
        a = actions[i]

        v2, a2 = MAX_VALUE_AB(game, game.RESULT(state, a), alpha, beta, depth + 1)

        if v2 < v:
            v = v2
            move = a

        if v <= alpha:
            pruned_branches += (len(actions) - i - 1)
            return v, move

        if v < beta:
            beta = v

    return v, move


# DISPLAY FUNCTIONS
# ============================================================

def print_board(state):
    print()
    print(" " + state[0] + " | " + state[1] + " | " + state[2])
    print("---+---+---")
    print(" " + state[3] + " | " + state[4] + " | " + state[5])
    print("---+---+---")
    print(" " + state[6] + " | " + state[7] + " | " + state[8])
    print()


def print_positions():
    print()
    print(" 0 | 1 | 2")
    print("---+---+---")
    print(" 3 | 4 | 5")
    print("---+---+---")
    print(" 6 | 7 | 8")
    print()


def board_to_string(state):
    s = ""
    for cell in state:
        if cell == ' ':
            s += '.'
        else:
            s += cell
    return s


# TREE VISUALIZATION WITH PRUNING

def visualize_alpha_beta(game, state, mode, alpha, beta, depth, max_depth, prefix):
    global player

    if game.IS_TERMINAL(state):
        print(prefix + board_to_string(state) + " -> Terminal, Utility = " + str(game.UTILITY(state, player)))
        return game.UTILITY(state, player)

    if depth > max_depth:
        print(prefix + board_to_string(state) + " -> Depth Limit")
        return 0

    actions = game.ACTIONS(state)

    if mode == "MAX":
        print(prefix + board_to_string(state) + " -> MAX [alpha=" + str(alpha) + ", beta=" + str(beta) + "]")
        v = -999999

        for i in range(len(actions)):
            a = actions[i]
            print(prefix + "  action = " + str(a))
            new_state = game.RESULT(state, a)

            v2 = visualize_alpha_beta(game, new_state, "MIN", alpha, beta, depth + 1, max_depth, prefix + "    ")

            if v2 > v:
                v = v2

            if v >= beta:
                print(prefix + "  PRUNE remaining branches after action " + str(a))
                return v

            if v > alpha:
                alpha = v

        return v

    else:
        print(prefix + board_to_string(state) + " -> MIN [alpha=" + str(alpha) + ", beta=" + str(beta) + "]")
        v = 999999

        for i in range(len(actions)):
            a = actions[i]
            print(prefix + "  action = " + str(a))
            new_state = game.RESULT(state, a)

            v2 = visualize_alpha_beta(game, new_state, "MAX", alpha, beta, depth + 1, max_depth, prefix + "    ")

            if v2 < v:
                v = v2

            if v <= alpha:
                print(prefix + "  PRUNE remaining branches after action " + str(a))
                return v

            if v < beta:
                beta = v

        return v


# ============================================================
# COMPARISON ON ONE STATE
# ============================================================

def compare_on_state(state, title):
    global minimax_nodes_explored, minimax_max_depth_reached
    global alphabeta_nodes_explored, alphabeta_max_depth_reached, pruned_branches

    game = TicTacToe()

    print("\n====================================")
    print(title)
    print("Board State:")
    print_board(state)

    # MINIMAX
    minimax_nodes_explored = 0
    minimax_max_depth_reached = 0

    start1 = time.time()
    move1 = MINIMAX_SEARCH(game, state)
    end1 = time.time()

    # ALPHA-BETA
    alphabeta_nodes_explored = 0
    alphabeta_max_depth_reached = 0
    pruned_branches = 0

    start2 = time.time()
    move2 = ALPHA_BETA_SEARCH(game, state)
    end2 = time.time()

    print("MINIMAX:")
    print("Best Move =", move1)
    print("Nodes Explored =", minimax_nodes_explored)
    print("Max Depth =", minimax_max_depth_reached)
    print("Time =", end1 - start1, "seconds")

    print("\nALPHA-BETA:")
    print("Best Move =", move2)
    print("Nodes Explored =", alphabeta_nodes_explored)
    print("Max Depth =", alphabeta_max_depth_reached)
    print("Pruned Branches =", pruned_branches)
    print("Time =", end2 - start2, "seconds")

    if minimax_nodes_explored != 0:
        saved = minimax_nodes_explored - alphabeta_nodes_explored
        percent = (saved * 100.0) / minimax_nodes_explored
        print("\nEfficiency Gain:")
        print("Nodes Saved =", saved)
        print("Reduction % =", percent)

    print("====================================")



# PRESET TEST CASES FOR VARIED GAME TREES


def run_varied_tree_analysis():
    # 1. Empty board -> very large tree
    state1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # 2. Mid-game balanced tree
    state2 = ['X', 'O', 'X',
              ' ', 'O', ' ',
              ' ', ' ', 'X']

    # 3. Near-endgame small tree
    state3 = ['X', 'O', 'X',
              'X', 'O', ' ',
              'O', 'X', ' ']

    compare_on_state(state1, "CASE 1: EMPTY BOARD (Largest Tree)")
    compare_on_state(state2, "CASE 2: MID-GAME BOARD")
    compare_on_state(state3, "CASE 3: NEAR-ENDGAME BOARD")

def play_game_alpha_beta():
    global alphabeta_nodes_explored, alphabeta_max_depth_reached, pruned_branches

    game = TicTacToe()
    state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    print("Human = X, AI = O (Alpha-Beta)")
    print_positions()

    while True:
        print_board(state)

        if game.TO_MOVE(state) == 'X':
            while True:
                move = input("Enter your move (0-8): ")
                if move.isdigit():
                    move = int(move)
                    if move in game.ACTIONS(state):
                        state = game.RESULT(state, move)
                        break
                print("Invalid move")
        else:
            alphabeta_nodes_explored = 0
            alphabeta_max_depth_reached = 0
            pruned_branches = 0

            start = time.time()
            move = ALPHA_BETA_SEARCH(game, state)
            end = time.time()

            print("AI chooses:", move)
            print("Nodes Explored:", alphabeta_nodes_explored)
            print("Max Depth Reached:", alphabeta_max_depth_reached)
            print("Pruned Branches:", pruned_branches)
            print("Decision Time:", end - start, "seconds")

            state = game.RESULT(state, move)

        if game.IS_TERMINAL(state):
            print_board(state)
            w = game.winner(state)

            if w is None:
                print("Draw")
            else:
                print("Winner:", w)
            break


# ============================================================
# SHOW ALPHA-BETA TREE
# ============================================================

def show_alpha_beta_tree():
    global player

    game = TicTacToe()
    state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    player = game.TO_MOVE(state)

    depth = input("Enter tree depth (recommended 1 or 2): ")
    if depth.isdigit():
        depth = int(depth)
        print("\nALPHA-BETA SEARCH TREE")
        visualize_alpha_beta(game, state, "MAX", -999999, 999999, 0, depth, "")
    else:
        print("Invalid depth")


def main():
    while True:
        print("\n1. Compare Minimax vs Alpha-Beta on Empty Board")
        print("2. Run Varied Game Tree Analysis")
        print("3. Visualize Alpha-Beta Search Tree")
        print("4. Play Game (AI uses Alpha-Beta)")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            compare_on_state(state, "EMPTY BOARD COMPARISON")

        elif choice == '2':
            run_varied_tree_analysis()

        elif choice == '3':
            show_alpha_beta_tree()

        elif choice == '4':
            play_game_alpha_beta()

        elif choice == '5':
            break

        else:
            print("Invalid choice")


main()