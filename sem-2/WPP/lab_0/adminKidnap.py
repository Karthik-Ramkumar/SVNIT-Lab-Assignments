T = int(input("Enter number of test cases: ")) 

for _ in range(T):
    X, N, S = map(int, input("Enter X, N, S: ").split())  
    current_position = X

    for _ in range(S):
        a, b = map(int, input("Enter swap pair (a b): ").split())
        if current_position == a:
            current_position = b
        elif current_position == b:
            current_position = a

    print("Final position of the gold coin:", current_position)