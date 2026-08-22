import re

class SimpleFST:
    def __init__(self):
        self.transitions = {}      # state -> { (input_char, output_char): next_state }
        self.final_outputs = {}    # state -> set of grammatical tags
        self.state_counter = 0
        self.start_state = self.new_state()

    def new_state(self):
        state = f"q{self.state_counter}"
        self.state_counter += 1
        self.transitions[state] = {}
        return state

    def add_transition(self, current, in_char, out_char):
        # Prefix sharing - reuse existing transition if present
        if (in_char, out_char) not in self.transitions[current]:
            self.transitions[current][(in_char, out_char)] = self.new_state()
        return self.transitions[current][(in_char, out_char)] # continue from new state

    def add_final(self, state, tag):
        if state not in self.final_outputs:
            self.final_outputs[state] = set() # set allows multiple outputs for one state
        self.final_outputs[state].add(tag)

    def minimize(self):
        # Bottom-up recursive minimization. Two states are identical if their outgoing transitions and final outputs are exactly the same.
        signature_to_state = {}

        def dfs(state):
            # Minimize all children first (bottom-up)
            # we minimize from the child upwards to parent
            # because when we compare two states their destination should be minimized
            for key, next_state in list(self.transitions[state].items()):
                self.transitions[state][key] = dfs(next_state)
                
            # build a unique "signature" for the current state
            trans_sig = tuple(sorted(self.transitions[state].items())) # all the transitions leaving the state
            final_sig = tuple(sorted(self.final_outputs.get(state, []))) # keeps whether state is final and what output it produces
            signature = (final_sig, trans_sig)
            
            # If we have seen this exact signature before -> merge,  Return the old state.
            if signature in signature_to_state:
                return signature_to_state[signature]
            else:
                signature_to_state[signature] = state
                return state

        self.start_state = dfs(self.start_state)

        # number of reachable states after minimization
        reachable = set() # all states reachable from the start state
        def find_reachable(state):
            if state in reachable: return
            reachable.add(state) # mark the state
            for next_state in self.transitions[state].values(): # visit all the destinations
                find_reachable(next_state)

        find_reachable(self.start_state)
        self.reachable_states = reachable # store final set of reachable states
        return len(reachable)

    def analyze(self, word):
        # stores: (current_state, current_index_in_word, accumulated_output)
        queue = [(self.start_state, 0, "")]
        results = set()
        
        while queue:
            state, idx, out_str = queue.pop(0)
            
            # Reached the end of the input word
            if idx == len(word):
                if state in self.final_outputs: # check if final state
                    for tag in self.final_outputs[state]:
                        results.add(out_str + tag) # get grammatical tag
                continue
                
            char = word[idx]
            for (in_char, out_char), next_state in self.transitions.get(state, {}).items():
                if in_char == char:
                    # If output is epsilon (ε), we don't add it to the final string
                    actual_out = "" if out_char == "ε" else out_char
                    queue.append((next_state, idx + 1, out_str + actual_out))
                    
        return ", ".join(sorted(results)) if results else "Invalid Word"


with open("brown_nouns.txt", "r", encoding="utf-8") as file:
    words = {line.strip() for line in file if re.fullmatch(r"[a-z]+", line.strip())}

fst = SimpleFST()

# Build the Trie
for word in words:
    
    # Add Singular Form
    curr = fst.start_state
    for char in word:
        curr = fst.add_transition(curr, char, char)
    fst.add_final(curr, "+N+SG")
    
    # Add Plural Form
    if word.endswith(("s", "x", "z", "ch", "sh")):
        plural = word + "es"
        plural_type = "es"
    elif word.endswith("y"):
        plural = word[:-1] + "ies"
        plural_type = "ies"
    else:
        plural = word + "s"
        plural_type = "s"
        
    curr = fst.start_state
    for i, char in enumerate(plural):
        # We output the root letters and silence the plural suffixes using ε (epsilon)
        if plural_type == "ies" and i >= len(word) - 1:
            out_char = 'y' if char == 'i' else 'ε'
        elif plural_type == "es" and i >= len(word):
            out_char = 'ε'
        elif plural_type == "s" and i >= len(word):
            out_char = 'ε'
        else:
            out_char = char
            
        curr = fst.add_transition(curr, char, out_char)
        
    fst.add_final(curr, "+N+PL")

states_before = len(fst.transitions)

states_after = fst.minimize()
#------------------------------------------------------------------------------------------

print(f"States BEFORE minimization: {states_before}")
print(f"States AFTER minimization:  {states_after}")

input_alphabet = set()
output_alphabet = set()

for state in fst.reachable_states:
    for (in_char, out_char) in fst.transitions[state].keys():
        input_alphabet.add(in_char)
        output_alphabet.add(out_char)
        
    for tag in fst.final_outputs.get(state, []):
        output_alphabet.add(tag)

print("\n Input Alphabet:",sorted(input_alphabet))
print("\n Output Alphabet:",sorted(output_alphabet))


# Transition Table
print(f"{'State':<10} | {'Input':<5} | {'Output':<10} | {'Next State / Final'}")
print("-" * 55)

count = 0
for state in fst.reachable_states:
    for (in_char, out_char), next_state in fst.transitions[state].items():
        if count < 15:
            print(f"{state:<10} | {in_char:<5} | {out_char:<10} | {next_state}")
            count += 1
            
    if state in fst.final_outputs and count < 20:
        for tag in fst.final_outputs[state]:
            print(f"{state:<10} | {'END':<5} | {tag:<10} | [FINAL]")
            count += 1
            
    if count >= 20:
        break


test_words = [
    "fox", "foxes", "bag", "bags", "try", "tries", 
    "dish", "dishes", "foxs", "dishs"
]

for word in test_words:
    print(f"{word:<8} -> {fst.analyze(word)}")