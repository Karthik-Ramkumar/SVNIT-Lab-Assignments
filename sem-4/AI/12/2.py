from collections import deque

# Hard Sudoku puzzle (0 = empty)
grid = [
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 5, 9, 0, 0, 0, 0, 0, 8],
    [2, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 4, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 3, 0, 5, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 2]
]

N = 9
TOTAL = 81

# Convert (row, col) <-> index

def idx(r, c):
    return r * 9 + c

def rc(index):
    return index // 9, index % 9

# Build adjacency matrix (81x81)
# 1 means Xi and Xj have constraint Xi != Xj
adj = [[0 for _ in range(TOTAL)] for _ in range(TOTAL)]

for r1 in range(9):
    for c1 in range(9):
        i = idx(r1, c1)
        for r2 in range(9):
            for c2 in range(9):
                j = idx(r2, c2)
                if i == j:
                    continue

                same_row = (r1 == r2)
                same_col = (c1 == c2)
                same_box = ((r1 // 3 == r2 // 3) and (c1 // 3 == c2 // 3))

                if same_row or same_col or same_box:
                    adj[i][j] = 1

# domains[i] = possible values for variable i
domains = [set() for _ in range(TOTAL)]

for r in range(9):
    for c in range(9):
        i = idx(r, c)
        if grid[r][c] == 0:
            domains[i] = set(range(1, 10))
        else:
            domains[i] = {grid[r][c]}

# Save initial domain sizes for statistics
initial_sizes = [len(domains[i]) for i in range(TOTAL)]

# REVISE(Xi, Xj) for Sudoku Xi != Xj
# Remove x from Di if no y in Dj satisfies x != y
# In Sudoku, this only happens when Dj = {x}
def revise(domains, xi, xj):
    revised = False
    to_remove = set()

    for x in domains[xi]:
        supported = False
        for y in domains[xj]:
            if x != y:
                supported = True
                break
        if not supported:
            to_remove.add(x)

    if to_remove:
        domains[xi] -= to_remove
        revised = True

    return revised, len(to_remove)

def ac3(domains, adj):
    queue = deque()
    total_removed = 0

    # Add all arcs (Xi, Xj) where constraint exists
    for i in range(TOTAL):
        for j in range(TOTAL):
            if adj[i][j] == 1:
                queue.append((i, j))

    while queue:
        xi, xj = queue.popleft()

        revised, removed_count = revise(domains, xi, xj)
        total_removed += removed_count

        if revised:
            if len(domains[xi]) == 0:
                return False, total_removed  # unsolvable

            # For every Xk neighbor of Xi except Xj, add (Xk, Xi)
            for xk in range(TOTAL):
                if adj[xk][xi] == 1 and xk != xj:
                    queue.append((xk, xi))

    return True, total_removed


result, total_removed = ac3(domains, adj)


arc_count = 0
for i in range(TOTAL):
    for j in range(TOTAL):
        if adj[i][j] == 1:
            arc_count += 1

#   If solved -> print value
#  Else print domain size
print("Sudoku AC-3 using Adjacency Matrix")
print("-" * 40)
print("Total directed arcs generated:", arc_count)
print("Total values removed from domains:", total_removed)
print("AC-3 status:", "Consistent" if result else "Domain reduced to zero (unsolvable by AC-3)")

print("\nRemaining Domain Size Grid (or solved value if singleton):")
for r in range(9):
    row_out = []
    for c in range(9):
        i = idx(r, c)
        if len(domains[i]) == 1:
            row_out.append(str(next(iter(domains[i]))))
        else:
            row_out.append(str(len(domains[i])))
    print(" ".join(row_out))


zero_domain = False
all_singleton = True

for i in range(TOTAL):
    if len(domains[i]) == 0:
        zero_domain = True
    if len(domains[i]) != 1:
        all_singleton = False

print("\nKey Result:")
if zero_domain:
    print("AC-3 reduced at least one domain to 0 -> puzzle is inconsistent / unsolvable under current constraints.")
elif all_singleton:
    print("AC-3 reduced all domains to 1 -> puzzle solved completely.")
else:
    print("AC-3 pruned the search space, but puzzle is not fully solved. Backtracking (or more inference) is still needed.")




print("\nRemaining Domains:")
for r in range(9):
    for c in range(9):
        i = idx(r, c)
        print(f"Cell ({r},{c}) -> {sorted(domains[i])}")