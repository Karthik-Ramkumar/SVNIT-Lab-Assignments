
def palindrom_check(word):
    left, right = 0, len(word) - 1
    count = 0
    while left < right:
        count += abs(ord(word[left]) - ord(word[right]))
        left += 1
        right -= 1
    return count

def main():
    num = int(input("Enter number of words"))
    for _ in range(num):
        word = input("Enter word: ").strip()
        print(palindrom_check(word))

if __name__ == "__main__":
    main()


    