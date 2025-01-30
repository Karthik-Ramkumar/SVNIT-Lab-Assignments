def root(len, n):
    digital_root = n  # Initialize digital_root

    while digital_root >= 10:  # Keep reducing until a single digit
        number_split = []
        temp = digital_root  # Use a temp variable to avoid modifying `n`
        digital_root = 0

        for _ in range(len):
            store = temp % 10
            number_split.append(store)
            temp //= 10

        for num in number_split:
            digital_root += num  # Sum all digits

        len = len(str(digital_root))  # Update length for new number

    return digital_root


def main():
    n = input("Enter number: ")
    length = len(n)
    n = int(n)
    root_n = root(length, n)
    print("Digital Root:", root_n)


main()
