from collections import deque

# constraints --> Xi != Xj

variables = ["P1", "P2", "P3", "P4", "P5", "P6"]

# helps quickly find the position of any project in the matrix.
var_index = {var: i for i, var in enumerate(variables)}

# P1 is already fixed to R1, while the others can still take any room.
domains = {
    "P1": {"R1"},
    "P2": {"R1", "R2", "R3"},
    "P3": {"R1", "R2", "R3"},
    "P4": {"R1", "R2", "R3"},
    "P5": {"R1", "R2", "R3"},
    "P6": {"R1", "R2", "R3"}
}

constraint_matrix = [
    # P1 P2 P3 P4 P5 P6
    [0, 1, 1, 0, 0, 1],  # P1
    [1, 0, 1, 1, 0, 0],  # P2
    [1, 1, 0, 0, 1, 0],  # P3
    [0, 1, 0, 0, 0, 1],  # P4
    [0, 0, 1, 0, 0, 1],  # P5
    [1, 0, 0, 1, 1, 0]   # P6
]

# Returns all neighboring projects connected to the given project.
def get_neighbors_connected(var):
    i = var_index[var]
    return [variables[j] for j, connected in enumerate(constraint_matrix[i]) if connected == 1]

# The revise step checks whether the domain of xi needs to be reduced
# because of the constraint between Xi and Xj.
# Here the constraint is Xi != Xj.
def revise(domains, xi, xj):
    revised = False
    to_remove = set()

    # For every possible value in xi's domain, check if there is
    # at least one different value in xj's domain that supports it.
    for x in domains[xi]:
        supported = False
        for y in domains[xj]:
            if x != y:
                supported = True
                break
        # If no supporting value is found, remove x from xi's domain.
        if not supported:
            to_remove.add(x)

    # Apply the removals if needed.
    if to_remove:
        domains[xi] -= to_remove
        revised = True

    return revised, to_remove


# AC-3 removes values that are not arc-consistent.
# It keeps checking connected variables until no more changes happen.
def ac3(domains):
    queue = deque()
    trace = []
    step_count = 0

    # Start by adding every connected pair from the adjacency matrix.
    for xi in variables:
        for xj in get_neighbors_connected(xi):
            queue.append((xi, xj))

    # Process each arc in the queue until there are no more arcs left.
    while queue:
        xi, xj = queue.popleft()
        revised, removed = revise(domains, xi, xj)

        # Store only the first five steps so the output stays short.
        if step_count < 5:
            if revised:
                trace.append(
                    f"Arc ({xi},{xj}) checked -> removed {sorted(list(removed))} from {xi}, new domain = {sorted(list(domains[xi]))}"
                )
            else:
                trace.append(f"Arc ({xi},{xj}) checked -> no change")
            step_count += 1

        # If a domain becomes empty, the CSP cannot be satisfied.
        if len(domains[xi]) == 0:
            return False, trace, domains

        # If xi changed, its other neighbors must be checked again.
        if revised:
            for xk in get_neighbors_connected(xi):
                if xk != xj:
                    queue.append((xk, xi))

    return True, trace, domains


# Prints the current domain of each project in a readable format.
def print_domains(domains):
    for var in variables:
        print(f"{var}: {sorted(list(domains[var]))}")


# Main program starts here.
# First, we show the initial domains.
print("Initial Domains (with P1 = R1):")
print_domains(domains)

# Run AC-3 on the current domains.
consistent, trace, final_domains = ac3(domains)

# Show the first few arc-reduction steps that were recorded.
print("\nFirst 5 Arc-Reduction Trace Steps:")
for i, t in enumerate(trace, 1):
    print(f"{i}. {t}")

# Show the final domains after AC-3 finishes.
print("\nFinal Domains After AC-3:")
print_domains(final_domains)

# Print whether the CSP stayed consistent or failed.
print("\nConsistency Check:")
if consistent:
    print("The CSP is arc-consistent after AC-3.")
    print("AC-3 does NOT detect failure. A valid set of domains remains.")
else:
    print("AC-3 detects failure (some domain became empty).")