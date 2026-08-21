import re

# Load Brown noun corpus
with open("brown_nouns.txt", "r", encoding="utf-8") as file:
    words = {
        line.strip()
        for line in file
        if re.fullmatch(r"[a-z]+", line.strip())
    }

print("number of words in corpus:", len(words))


def get_plural(word):

    # -es rule comes first
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return [word + "es"]

    # -ies rule
    if word.endswith("y"):
        return [word[:-1] + "ies"]

    # normal -s rule
    return [word + "s"]


def analyze(word):

    for root in words:

        if word in get_plural(root):
            return root + "+N+PL"

    if word in words:
        return word + "+N+SG"

    return "Invalid Word"

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