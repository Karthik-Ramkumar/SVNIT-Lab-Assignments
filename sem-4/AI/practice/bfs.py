def bfs(adj_matrix, start):
    n = len(adj_matrix)
    visited = [False] * n
    queue = []

    visited[start] = True
    queue.append(start)

    print("BFS Traversal:", end=" ")
    #nodes_explored = 0
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        #nodes_explored += 1
        
        for i in range(n):
            if adj_matrix[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)
    
    
    #print(f"\nTotal nodes explored: {nodes_explored}")
                
# Example
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

start_node = 0
bfs(adj_matrix, start_node)
print()