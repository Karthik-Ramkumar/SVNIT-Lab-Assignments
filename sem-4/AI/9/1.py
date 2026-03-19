import time
import random

player = None
nodes_explored = 0
max_depth_reached = 0


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


def MINIMAX_SEARCH(game, state):
    global player
    player = game.TO_MOVE(state)
    value, move = MAX_VALUE(game, state, 0)
    return move


def MAX_VALUE(game, state, depth):
    global nodes_explored, max_depth_reached, player

    nodes_explored += 1
    if depth > max_depth_reached:
        max_depth_reached = depth

    if game.IS_TERMINAL(state):
        return game.UTILITY(state, player), None

    v = -999999
    move = None

    for a in game.ACTIONS(state):
        v2, a2 = MIN_VALUE(game, game.RESULT(state, a), depth + 1)

        if v2 > v:
            v = v2
            move = a

    return v, move


def MIN_VALUE(game, state, depth):
    global nodes_explored, max_depth_reached, player

    nodes_explored += 1
    if depth > max_depth_reached:
        max_depth_reached = depth

    if game.IS_TERMINAL(state):
        return game.UTILITY(state, player), None

    v = 999999
    move = None

    for a in game.ACTIONS(state):
        v2, a2 = MAX_VALUE(game, game.RESULT(state, a), depth + 1)

        if v2 < v:
            v = v2
            move = a

    return v, move


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


def evaluate_partial_state(game, state):
    if game.IS_TERMINAL(state):
        return game.UTILITY(state, player)
    return "Cutoff"


def visualize_tree(game, state, mode, depth, max_depth, prefix, is_last, action_taken):
    branch = ""
    child_prefix = ""

    if depth == 0:
        branch = "ROOT "
        child_prefix = ""
    else:
        if is_last:
            branch = prefix + "└── "
            child_prefix = prefix + "    "
        else:
            branch = prefix + "├── "
            child_prefix = prefix + "│   "

    node_info = board_to_string(state)

    if game.IS_TERMINAL(state):
        utility = game.UTILITY(state, player)
        if depth == 0:
            print(branch + node_info + " [" + mode + "] -> Terminal, Utility = " + str(utility))
        else:
            print(branch + "action " + str(action_taken) + " -> " + node_info + " [" + mode + "] -> Terminal, Utility = " + str(utility))
        return

    if depth == max_depth:
        cutoff_value = evaluate_partial_state(game, state)
        if depth == 0:
            print(branch + node_info + " [" + mode + "] -> Depth Limit, Value = " + str(cutoff_value))
        else:
            print(branch + "action " + str(action_taken) + " -> " + node_info + " [" + mode + "] -> Depth Limit, Value = " + str(cutoff_value))
        return

    if depth == 0:
        print(branch + node_info + " [" + mode + "]")
    else:
        print(branch + "action " + str(action_taken) + " -> " + node_info + " [" + mode + "]")

    actions = game.ACTIONS(state)
    random.shuffle(actions)

    next_mode = "MIN"
    if mode == "MIN":
        next_mode = "MAX"

    total_actions = len(actions)

    for i in range(total_actions):
        a = actions[i]
        new_state = game.RESULT(state, a)

        if i == total_actions - 1:
            child_is_last = True
        else:
            child_is_last = False

        visualize_tree(game, new_state, next_mode, depth + 1, max_depth, child_prefix, child_is_last, a)


def performance_test():
    global nodes_explored, max_depth_reached

    game = TicTacToe()
    state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    nodes_explored = 0
    max_depth_reached = 0

    start = time.time()
    move = MINIMAX_SEARCH(game, state)
    end = time.time()

    print("\nPERFORMANCE TEST")
    print_board(state)
    print("Best Move:", move)
    print("Nodes Explored:", nodes_explored)
    print("Max Depth Reached:", max_depth_reached)
    print("Execution Time:", end - start, "seconds")


def play_game():
    global nodes_explored, max_depth_reached

    game = TicTacToe()
    state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    print("Human = X, AI = O")
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
            nodes_explored = 0
            max_depth_reached = 0

            start = time.time()
            move = MINIMAX_SEARCH(game, state)
            end = time.time()

            print("AI chooses:", move)
            print("Nodes Explored:", nodes_explored)
            print("Max Depth Reached:", max_depth_reached)
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


def show_tree():
    global player

    game = TicTacToe()
    state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    player = game.TO_MOVE(state)

    depth = input("Enter tree depth (recommended 1, 2, or 3): ")
    if depth.isdigit():
        depth = int(depth)

        seed_choice = input("Enter random seed (or press Enter for random tree): ")

        if seed_choice.strip() != "":
            if seed_choice.isdigit():
                random.seed(int(seed_choice))
            else:
                print("Invalid seed, using random order")

        print("\nSEARCH TREE")
        visualize_tree(game, state, "MAX", 0, depth, "", True, None)
    else:
        print("Invalid depth")


def main():
    while True:
        print("\n1. Performance Test")
        print("2. Visualize Search Tree (Upgraded)")
        print("3. Play Game")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            performance_test()
        elif choice == '2':
            show_tree()
        elif choice == '3':
            play_game()
        elif choice == '4':
            break
        else:
            print("Invalid choice")


main()