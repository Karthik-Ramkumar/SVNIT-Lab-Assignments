def backward_chaining_case1(goal, facts):
    if goal in facts:
        print(f"{goal} is a known fact")
        return True

    if goal == "Q":
        print("Trying to prove Q using P → Q or R → Q")
        return backward_chaining_case1("P", facts) or backward_chaining_case1("R", facts)

    elif goal == "P":
        print("Trying to prove P using A → P")
        return backward_chaining_case1("A", facts)

    elif goal == "R":
        print("Trying to prove R using B → R")
        return backward_chaining_case1("B", facts)

    print(f"Failed to prove {goal}")
    return False


def backward_chaining_case2(goal, facts):
    if goal in facts:
        print(f"{goal} is a known fact")
        return True

    if goal == "D":
        print("Trying to prove D using B ∧ C → D")
        return backward_chaining_case2("B", facts) and backward_chaining_case2("C", facts)

    elif goal == "B":
        print("Trying to prove B using A → B")
        return backward_chaining_case2("A", facts)

    elif goal == "C":
        print("Trying to prove C using E → C")
        return backward_chaining_case2("E", facts)

    print(f"Failed to prove {goal}")
    return False


choice = int(input("Backward Chaining\n1. Question 2(a)\n2. Question 2(b)\nEnter choice: "))

if choice == 1:
    facts = {"A", "B"}
    result = backward_chaining_case1("Q", facts)
    if result:
        print("\nConclusion Q is TRUE")
    else:
        print("\nConclusion Q is FALSE")

elif choice == 2:
    facts = {"A", "E"}
    result = backward_chaining_case2("D", facts)
    if result:
        print("\nConclusion D is TRUE")
    else:
        print("\nConclusion D is FALSE")

else:
    print("Invalid choice")