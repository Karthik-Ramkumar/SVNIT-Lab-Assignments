distance = [
# Chi Det Cle Ind Col Pit Buf Syr NY  Phi Bal Bos Pro Por
[  0,283,345,182,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # chi
[283,  0,169,  0,  0,  0,256,  0,  0,  0,  0,  0,  0,  0], # det
[345,169,  0,  0,144,134,189,  0,  0,  0,  0,  0,  0,  0], # cle
[182,  0,  0,  0,176,  0,  0,  0,  0,  0,  0,  0,  0,  0], # ind
[  0,  0,144,176,  0,185,  0,  0,  0,  0,  0,  0,  0,  0], # col
[  0,  0,134,  0,185,  0,215,  0,  0,305,247,  0,  0,  0], # pit
[  0,256,189,  0,  0,215,  0,150,  0,  0,  0,  0,  0,  0], # buf
[  0,  0,  0,  0,  0,  0,150,  0,254,253,  0,312,  0,  0], # syr
[  0,  0,  0,  0,  0,  0,  0,254,  0, 97,  0,  0,181,  0], # ny
[  0,  0,  0,  0,  0,305,  0,253, 97,  0,101,215,  0,  0], # phi
[  0,  0,  0,  0,  0,247,  0,  0,  0,101,  0,  0,  0,  0], # bal
[  0,  0,  0,  0,  0,  0,  0,312,  0,215,  0,  0, 50,107], # bos
[  0,  0,  0,  0,  0,  0,  0,  0,181,  0,  0, 50,  0,  0], # pro
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,107,  0,  0]  # por
]

States = {
    0: "Chicago", 1: "Detroit", 2: "Cleveland", 3: "Columbus", 4: "Indianapolis",
    5: "Buffalo", 6: "Pittsburgh", 7: "Syracuse", 8: "New York", 9: "Philadelphia",
    10: "Baltimore", 11: "Boston", 12: "Providence", 13: "Portland"
}

START = 0
GOAL = 11

nodes_explored = 0
PRINT_EVERY = 5

best_cost_global = float('inf')
best_path_global = []


def neighbors(city):
    return [(i, distance[city][i]) for i in range(len(distance)) if distance[city][i] > 0]


def alphabeta_style(city, visited, path, cost_so_far, depth=0):
    global nodes_explored, best_cost_global, best_path_global

    nodes_explored += 1

    if nodes_explored % PRINT_EVERY == 0:
        print(f"[Search] Node #{nodes_explored} | Depth={depth} | Current={States[city]} | CostSoFar={cost_so_far} | BestKnown={best_cost_global}")

    # prune if already worse than best known complete path
    if cost_so_far >= best_cost_global:
        print(f"[Prune] At {States[city]} because CostSoFar={cost_so_far} >= BestKnown={best_cost_global}")
        return

    # goal reached
    if city == GOAL:
        print(f"[Goal] Reached {States[city]} | Total Cost={cost_so_far}")
        if cost_so_far < best_cost_global:
            best_cost_global = cost_so_far
            best_path_global = path.copy()
            print(f"[Update] New BEST PATH = {' -> '.join(States[i] for i in best_path_global)} | Cost={best_cost_global}")
        return

    # sort neighbors by edge cost (helps pruning happen earlier)
    next_nodes = neighbors(city)
    next_nodes.sort(key=lambda x: x[1])

    for nxt, edge_cost in next_nodes:
        if nxt not in visited:
            visited.add(nxt)
            path.append(nxt)

            alphabeta_style(nxt, visited, path, cost_so_far + edge_cost, depth + 1)

            path.pop()
            visited.remove(nxt)


def run():
    global best_cost_global, best_path_global, nodes_explored

    best_cost_global = float('inf')
    best_path_global = []
    nodes_explored = 0

    alphabeta_style(START, {START}, [START], 0, 0)

    return best_cost_global, best_path_global


if __name__ == "__main__":
    final_cost, final_path = run()

    if final_path:
        print("\nOptimal Path:")
        print(" -> ".join(States[i] for i in final_path))
        print("Cost:", final_cost)
    else:
        print("\nNo path found")

    print("\nNodes Explored:", nodes_explored)