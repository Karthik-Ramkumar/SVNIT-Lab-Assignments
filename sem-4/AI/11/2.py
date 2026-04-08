# Cryptarithmetic CSP: SEND + MORE = MONEY
# Each letter has a unique digit
# S and M cannot be 0

letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
used = [0] * 10
solution_found = 0

def solve(index, values):
    global solution_found

    if solution_found == 1:
        return

    if index == len(letters):
        S = values['S']
        E = values['E']
        N = values['N']
        D = values['D']
        M = values['M']
        O = values['O']
        R = values['R']
        Y = values['Y']

        send = S * 1000 + E * 100 + N * 10 + D
        more = M * 1000 + O * 100 + R * 10 + E
        money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y

        if send + more == money:
            print("Solution found:\n")
            print("S =", S)
            print("E =", E)
            print("N =", N)
            print("D =", D)
            print("M =", M)
            print("O =", O)
            print("R =", R)
            print("Y =", Y)

            print("\nSEND  =", send)
            print("MORE  =", more)
            print("MONEY =", money)

            solution_found = 1

        return

    ch = letters[index]

    for digit in range(10):
        if used[digit] == 0:
            if (ch == 'S' or ch == 'M') and digit == 0:
                continue

            values[ch] = digit
            used[digit] = 1

            solve(index + 1, values)

            used[digit] = 0
            del values[ch]

values = {}
solve(0, values)

if solution_found == 0:
    print("No solution found.")