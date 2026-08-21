def is_valid_word(word):
    state = "q0"
    for char in word:
        if state == "q0":
            if 'a' <= char <= 'z':
                state = "q1"
            else:
                return False

        elif state == "q1":
            if 'a' <= char <= 'z':
                state = "q1"
            else:
                return False

    return state == "q1"

word = input("word: ")

if is_valid_word(word):
    print("accepted")
else:
    print("not accepted")