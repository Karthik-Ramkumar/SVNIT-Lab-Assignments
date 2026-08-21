import re

# Load Brown noun corpus
with open("brown_nouns.txt", "r", encoding="utf-8") as file:
    words = {
        line.strip()
        for line in file
        if re.fullmatch(r"[a-z]+", line.strip())
    }

print("Number of words in corpus:", len(words))


def get_plural_forms(word):

    # -es rule comes first
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return [word + "es"]

    # -ies rule
    if word.endswith("y"):
        return [word[:-1] + "ies"]

    # normal -s rule
    return [word + "s"]


def analyze(word):

    # Check whether the word can be a plural FIRST
    for root in words:

        if word in get_plural_forms(root):
            return root + "+N+PL"

    # If it wasn't a plural, check if it is a noun
    if word in words:
        return word + "+N+SG"

    return "Invalid Word"


# Test
test_words = [
    "fox",
    "foxes",
    "bag",
    "bags",
    "try",
    "tries",
    "foxs",
    "dishs"
]

for word in test_words:
    print(word, "->", analyze(word))