from collections import defaultdict, deque

graph = defaultdict(list)

def BFS(start, destination):
    q = deque()
    q.append(([start], 0))

    print("\nBFS Paths:")

    while q:
        path, cost = q.popleft()
        last_city = path[-1] #last element of list

        if last_city == destination:
            print("Path:", " -> ".join(path), f"| Cost = {cost} miles")
            continue

        for neighbour, dist in graph[last_city]:
            if neighbour not in path:               #prevention of not going to same city again
                new_path = path + [neighbour]       #making new path
                q.append((new_path, cost + dist))

def DFS(current, destination, visited, path, cost):
    if current == destination:
        print("Path:", " -> ".join(path), f"| Cost = {cost} miles")
        return

    visited[current] = True

    for neighbour, dist in graph[current]:  #graph is directed, edges exist only in one direction
        if not visited.get(neighbour, False):
            path.append(neighbour)
            DFS(neighbour, destination, visited, path, cost + dist)
            path.pop()

    visited[current] = False

#dfs recursive | bfs queue ,level order
#assuming all directions point towards chicago
#graph is directed, edges exist only in one direction
# with fixed neighbour order and limited branching here i will get same paths for bfs and fds 

#BFS FASTER 

if __name__ == "__main__":
    graph["Syracuse"] = [("Buffalo",150), ("New York",254),("Philadelphia",253),("Boston",312)]
    graph["Buffalo"] = [("Detroit",256), ("Cleveland",189), ("Pittsburgh",215)]
    graph["Detroit"] = [("Chicago",283)]
    graph["Cleveland"] = [("Chicago",345), ("Detroit",169), ("Columbus",144)]
    graph["Columbus"] = [("Indianapolis",176)]
    graph["Indianapolis"] = [("Chicago",182)]
    graph["Pittsburgh"] = [("Columbus",185),("Cleveland",134)]
    graph["Philadelphia"] = [("Pittsburgh",305), ("Baltimore",101)]
    graph["New York"] = [("Philadelphia",97)]
    graph["Baltimore"] = [("Pittsburgh",247)]

    start = "Syracuse"
    destination = "Chicago"

    print("DFS Paths:")
    visited = {}
    DFS(start, destination, visited, [start], 0)

    BFS(start, destination)
