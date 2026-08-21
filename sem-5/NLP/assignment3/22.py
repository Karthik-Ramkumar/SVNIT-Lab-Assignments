import re
with open("brown_nouns.txt", "r", encoding="utf-8") as file:
    vocabulary = {
        line.strip()
        for line in file
        if re.fullmatch(r"[a-z]+", line.strip())
    }


class FST:
    def __init__(self):
        self.transitions = {}
        self.states = set()
        self.final_outputs = {}

        self.start_state = "q0"
        self.state_count = 1

        self.states.add("q0")

    def new_state(self):
        state = f"q{self.state_count}"
        self.state_count += 1
        self.states.add(state)
        return state

    def add_transition(self, current, input_symbol,
                       output_symbol, next_state):

        self.transitions[(current, input_symbol)] = (
            output_symbol,
            next_state
        )

    def add_final_output(self, state, output):
        self.final_outputs[state] = output


fst = FST()

# Each node stores the FST state associated with it
root = {"state": "q0", "children": {}}

# Only words that can act as roots
roots = set(vocabulary)

for word in roots:

    node = root

    for character in word:

        if character not in node["children"]:

            next_state = fst.new_state()

            node["children"][character] = {
                "state": next_state,
                "children": {}
            }

            fst.add_transition(
                node["state"],
                character,
                character,
                next_state
            )

        node = node["children"][character]

for root_word in roots:

    node = root

    for character in root_word:
        node = node["children"][character]

    state = node["state"]

    # Singular
    if root_word in vocabulary:
        fst.add_final_output(
            state,
            "+N+SG"
        )

    # Plural: root + s
    plural_s = root_word + "s"

    if plural_s in vocabulary:
        plural_state = fst.new_state()

        fst.add_transition(
            state,
            "s",
            "s",
            plural_state
        )

        fst.add_final_output(
            plural_state,
            "+N+PL"
        )

    # Plural: root + es
    plural_es = root_word + "es"

    if plural_es in vocabulary:

        e_state = fst.new_state()
        s_state = fst.new_state()

        fst.add_transition(
            state,
            "e",
            "e",
            e_state
        )

        fst.add_transition(
            e_state,
            "s",
            "s",
            s_state
        )

        fst.add_final_output(
            s_state,
            "+N+PL"
        )

    # Plural: y -> ies
    if root_word.endswith("y"):

        plural_ies = root_word[:-1] + "ies"

        if plural_ies in vocabulary:

            # Go back to the state before y
            node = root

            for character in root_word[:-1]:
                node = node["children"][character]

            state_before_y = node["state"]

            i_state = fst.new_state()
            e_state = fst.new_state()
            s_state = fst.new_state()

            fst.add_transition(
                state_before_y,
                "i",
                "i",
                i_state
            )

            fst.add_transition(
                i_state,
                "e",
                "e",
                e_state
            )

            fst.add_transition(
                e_state,
                "s",
                "s",
                s_state
            )

            fst.add_final_output(
                s_state,
                "+N+PL"
            )

def analyze(word):

    state = fst.start_state
    output = ""

    for character in word:

        transition = fst.transitions.get(
            (state, character)
        )

        if transition is None:
            return "Invalid Word"

        output_symbol, state = transition

        output += output_symbol

    if state in fst.final_outputs:

        output += fst.final_outputs[state]

        # Recover the lexical root from the output
        if output.endswith("+N+SG"):
            root = word

        else:
            root = word

            if word.endswith("ies"):
                root = word[:-3] + "y"

            elif word.endswith("es"):
                root = word[:-2]

            elif word.endswith("s"):
                root = word[:-1]

        return root + output

    return "Invalid Word"

print("Transition Table")

for (state, input_symbol), (output_symbol, next_state) in fst.transitions.items():

    print(
        state,
        input_symbol + ":" + output_symbol,
        next_state
    )


input_alphabet = set()

for state, symbol in fst.transitions:
    input_alphabet.add(symbol)

output_alphabet = set()

for _, output_symbol in fst.transitions.values():
    output_alphabet.add(output_symbol)

output_alphabet.update(fst.final_outputs.values())

print("\nInput Alphabet:")
print(sorted(input_alphabet))

print("\nOutput Alphabet:")
print(sorted(output_alphabet))

print("\nNumber of states:", len(fst.states))

test_words = [
    "fox",
    "foxes",
    "bag",
    "bags",
    "try",
    "tries",
    "dish",
    "dishes",
    "foxs",
    "dishs"
]

print("\nResults")

for word in test_words:
    print(word, "->", analyze(word))