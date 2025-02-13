word = input("Enter word: ")
lexGreater = list(word)

for i in range(len(word) - 1):
    if word[i] < word[i + 1]:
        lexGreater[i], lexGreater[i + 1] = lexGreater[i + 1], lexGreater[i]
        break

print("".join(lexGreater))
