from collections import deque

graph = {
    "Raj": ["Priya", "Akash"],
    "Priya": ["Raj", "Aarav", "Neha1"],
    "Akash": ["Raj", "Sunil"],
    "Sunil": ["Akash", "Sneha"],
    "Sneha": ["Sunil", "Rahul"],
    "Rahul": ["Sneha", "Neha1", "Pooja", "Maya"],
    "Neha1": ["Priya", "Rahul", "Aarav"],
    "Aarav": ["Priya", "Neha2"],
    "Neha2": ["Aarav", "Arjun"],
    "Arjun": ["Neha2", "Pooja"],
    "Pooja": ["Arjun", "Rahul"],
    "Maya": ["Rahul"]
}

# BFS
def bfs(start):
    visited = set()
    q = deque([start])
    print("BFS order:")

    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for nbr in graph[node]:
                if nbr not in visited:
                    q.append(nbr)
    print()

# DFS
def dfs(node, visited):
    print(node, end=" ")
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            dfs(nbr, visited)

# Run
start = "Raj"
bfs(start)

print("DFS order:")
dfs(start, set())
print("\n")




















































'''from collections import deque

adj = []
visited = []

def BFS(start, V):
    visited_bfs = [False] * V
    q = deque()

    visited_bfs[start] = True
    q.append(start)

    while q:
        node = q.popleft()
        print(node, end=" ")

        for neighbor in adj[node]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                q.append(neighbor)

def DFS(node):
    visited[node] = True
    print(node, end=" ")

    for neighbor in adj[node]:
        if not visited[neighbor]:
            DFS(neighbor)



if __name__ == "__main__":
    V = 11
    adj = [[] for _ in range(V)]
    visited = [False] * V

    # Directed edges
    adj[0].extend([1, 2, 3, 4])
    adj[1].extend([5, 6])
    adj[2].extend([7, 8])
    adj[3].append(10)
    adj[4].append(9)

    start = 0

    print("BFS Traversal:", end=" ")
    BFS(start, V)
    print()

    print("DFS Traversal:", end=" ")
    DFS(start)
    print()
'''