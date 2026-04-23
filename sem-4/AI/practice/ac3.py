# AC-3 Algorithm (simple version)

from collections import deque

def revise(xi, xj, domains):
    revised = False

    for x in domains[xi][:]:
        found = False

        for y in domains[xj]:
            if x != y:   # constraint: neighboring nodes must have different values
                found = True
                break

        if not found:
            domains[xi].remove(x)
            revised = True

    return revised

def ac3(variables, domains, neighbors):
    queue = deque()

    for xi in variables:
        for xj in neighbors[xi]:
            queue.append((xi, xj))

    while queue:
        xi, xj = queue.popleft()

        if revise(xi, xj, domains):
            if len(domains[xi]) == 0:
                return False

            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True


# Example
variables = ['A', 'B', 'C']

domains = {
    'A': [1, 2, 3],
    'B': [2],
    'C': [1, 2, 3]
}

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

if ac3(variables, domains, neighbors):
    print("Consistent Domains:", domains)
else:
    print("No solution")