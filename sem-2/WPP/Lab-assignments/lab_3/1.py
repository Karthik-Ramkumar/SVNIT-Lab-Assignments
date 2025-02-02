def root(num_len, num):
    digital_root = num  

    while digital_root >= 10:  
        number_split = []
        temp = digital_root 
        digital_root = 0

        for _ in range(num_len):
            store = temp % 10
            number_split.append(store)
            temp //= 10

        for num in number_split:
            digital_root += num  

        num_len = len(str(digital_root))  

    return digital_root


def main():
    num = input("Enter number: ")
    num_len = len(num)  
    num = int(num)
    root_n = root(num_len, num)
    print("Digital Root:", root_n)


main()
