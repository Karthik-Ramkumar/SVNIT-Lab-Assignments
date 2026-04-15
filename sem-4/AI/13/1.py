from itertools import product

# ---------------- SYMBOL CLASS ----------------
class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


P = Symbol('P')
Q = Symbol('Q')
R = Symbol('R')
# If needed, you can also create named negation symbols like:
# notP = Symbol('negation of P')
# notQ = Symbol('negation of Q')


def op_not(a):
    return not a

def op_and(a, b):
    return a and b

def op_or(a, b):
    return a or b

def op_implies(a, b):
    return (not a) or b

def op_biconditional(a, b):
    return a == b


def is_symbol(token):
    return token in ['P', 'Q', 'R']

def is_operator(token):
    return token in ['~', '^', 'v', '->', '<->']

def precedence(op):
    if op == '~':
        return 4
    elif op == '^':
        return 3
    elif op == 'v':
        return 2
    elif op == '->':
        return 1
    elif op == '<->':
        return 0
    return -1

def is_right_associative(op):
    return op in ['~', '->', '<->']


def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            i += 1
            continue

        if expr[i] in ['(', ')', '^', 'v', '~']:
            tokens.append(expr[i])
            i += 1
        elif expr[i] == '-' and i + 1 < len(expr) and expr[i + 1] == '>':
            tokens.append('->')
            i += 2
        elif expr[i] == '<' and i + 2 < len(expr) and expr[i + 1] == '-' and expr[i + 2] == '>':
            tokens.append('<->')
            i += 3
        elif expr[i] in ['P', 'Q', 'R']:
            tokens.append(expr[i])
            i += 1
        else:
            raise ValueError(f"Invalid character in expression: {expr[i]}")
    return tokens


def infix_to_postfix(expr):
    tokens = tokenize(expr)
    output = []
    stack = []

    for token in tokens:
        if is_symbol(token):
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()

        elif is_operator(token):
            while (
                stack and stack[-1] != '(' and
                (
                    precedence(stack[-1]) > precedence(token) or
                    (
                        precedence(stack[-1]) == precedence(token) and
                        not is_right_associative(token)
                    )
                )
            ):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        if stack[-1] in ['(', ')']:
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return output


def evaluate_postfix(postfix, values):
    stack = []

    for token in postfix:
        if is_symbol(token):
            stack.append(values[token])

        elif token == '~':  # unary
            a = stack.pop()
            stack.append(op_not(a))

        elif token == '^':
            b = stack.pop()
            a = stack.pop()
            stack.append(op_and(a, b))

        elif token == 'v':
            b = stack.pop()
            a = stack.pop()
            stack.append(op_or(a, b))

        elif token == '->':
            b = stack.pop()
            a = stack.pop()
            stack.append(op_implies(a, b))

        elif token == '<->':
            b = stack.pop()
            a = stack.pop()
            stack.append(op_biconditional(a, b))

    return stack[0]


def get_used_symbols(postfix):
    used = []
    for token in postfix:
        if token in ['P', 'Q', 'R'] and token not in used:
            used.append(token)
    return used


# boolean display 
def tf(x):
    return 'T' if x else 'F'


def print_truth_table(expr):
    postfix = infix_to_postfix(expr)
    used_symbols = get_used_symbols(postfix)

    print(f"\nInfix   : {expr}")
    print(f"Postfix : {' '.join(postfix)}")

    header = " | ".join(used_symbols) + " | " + expr
    print("\n" + header)
    print("-" * len(header))

    for vals in product([False, True], repeat=len(used_symbols)):
        value_map = {}
        for i in range(len(used_symbols)):
            value_map[used_symbols[i]] = vals[i]

        result = evaluate_postfix(postfix, value_map)

        row = " | ".join(tf(value_map[s]) for s in used_symbols)
        row += " | " + tf(result)
        print(row)


def main():
    statements = [
        "~P->Q",
        "~P^~Q",
        "~Pv~Q",
        "~P->~Q",
        "~P<->~Q",
        "(PvQ)^(~P->Q)",
        "((PvQ)->~R)",
        "(((PvQ)->~R)<->((~P^~Q)->~R))",
        "(((P->Q)^(Q->R))->(Q->R))",
        "((P->(QvR))->(~P^~Q^~R))"
    ]

    for stmt in statements:
        print_truth_table(stmt)


if __name__ == "__main__":
    main()