def resolution(case):
    if case == 1:
        print("\nQuestion 3(a)")
        print("Knowledge Base:")
        print("1. P ∨ Q")
        print("2. ¬P ∨ R   (from P → R)")
        print("3. ¬Q ∨ S   (from Q → S)")
        print("4. ¬R ∨ S   (from R → S)")
        print("Negated Conclusion:")
        print("5. ¬S")

        print("\nResolution Steps:")
        print("6. From (3) and (5): ¬Q")
        print("7. From (4) and (5): ¬R")
        print("8. From (2) and (7): ¬P")
        print("9. From (1) and (6): P")
        print("10. From (8) and (9): EMPTY CLAUSE {}")

        print("\nContradiction found")
        print("Therefore, conclusion S is TRUE")

    elif case == 2:
        print("\nQuestion 3(b)")
        print("Knowledge Base:")
        print("1. ¬P ∨ Q   (from P → Q)")
        print("2. ¬Q ∨ R   (from Q → R)")
        print("3. ¬S ∨ ¬R  (from S → ¬R)")
        print("4. P")
        print("Negated Conclusion:")
        print("5. ¬S")

        print("\nResolution Steps:")
        print("6. From (1) and (4): Q")
        print("7. From (2) and (6): R")
        print("8. From (3) and (5): ¬R")
        print("9. From (7) and (8): EMPTY CLAUSE {}")

        print("\nContradiction found")
        print("Therefore, conclusion S is TRUE")

    else:
        print("Invalid choice")


choice = int(input("Resolution / Proof by Refutation\n1. Question 3(a)\n2. Question 3(b)\nEnter choice: "))
resolution(choice)