def bellman_ford(adj_matrix, start):
    num_vertices = len(adj_matrix)
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v in range(num_vertices):
                weight = adj_matrix[u][v]
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    return distances

# Using adjacency matrix

adj_matrix = [
    [0, -1, 4, float('inf'), float('inf')],
    [float('inf'), 0, 3, 2, 2],
    [float('inf'), float('inf'), 0, float('inf'), float('inf')],
    [float('inf'), 1, 5, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), -3, 0]
]

source_vertex = 0

distances = bellman_ford(adj_matrix, source_vertex)
print(distances)
