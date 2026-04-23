# AND-OR Graph (simple recursive cost calculation)

graph = {
    'A': [('OR', ['B', 'C']), ('AND', ['D', 'E'])],
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 5
}

def and_or_search(node):
    if type(graph[node]) == int:
        return graph[node]

    best = 999

    for kind, children in graph[node]:
        if kind == 'OR':
            cost = min(and_or_search(child) for child in children)
        else:  # AND
            cost = sum(and_or_search(child) for child in children)

        if cost < best:
            best = cost

    return best


# Example
print("Minimum Cost:", and_or_search('A'))