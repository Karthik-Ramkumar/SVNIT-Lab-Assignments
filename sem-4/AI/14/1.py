def forward_chaining(case):
    facts = set()

    if case == 1:
        print("Question 1(a)")
        facts.update(["A", "B", "M"])

        changed = True
        while changed:
            changed = False

            if "A" in facts and "B" in facts and "L" not in facts:
                facts.add("L")
                print("Derived: L using A ∧ B → L")
                changed = True

            if "L" in facts and "M" in facts and "P" not in facts:
                facts.add("P")
                print("Derived: P using L ∧ M → P")
                changed = True

            if "P" in facts and "Q" not in facts:
                facts.add("Q")
                print("Derived: Q using P → Q")
                changed = True

        if "Q" in facts:
            print("\nConclusion Q is TRUE")
        else:
            print("\nConclusion Q is FALSE")

    elif case == 2:
        print("Question 1(b)")
        facts.update(["A", "E"])

        changed = True
        while changed:
            changed = False

            if "A" in facts and "B" not in facts:
                facts.add("B")
                print("Derived: B using A → B")
                changed = True

            if "B" in facts and "C" not in facts:
                facts.add("C")
                print("Derived: C using B → C")
                changed = True

            if "C" in facts and "D" not in facts:
                facts.add("D")
                print("Derived: D using C → D")
                changed = True

            if "D" in facts and "E" in facts and "F" not in facts:
                facts.add("F")
                print("Derived: F using D ∧ E → F")
                changed = True

        if "F" in facts:
            print("\nConclusion F is TRUE")
        else:
            print("\nConclusion F is FALSE")

    else:
        print("Invalid choice")

choice = int(input("Forward Chaining\n1. question 1(a)\n2. question 1(b)\nEnter choice: "))
forward_chaining(choice)