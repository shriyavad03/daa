def dijkstra(adj_matrix, start):
    num_vertices = len(adj_matrix)
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        # Find the vertex with the smallest distance among unvisited vertices
        min_distance = float('inf')
        min_vertex = None
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v
        
        if min_vertex is None:
            break
        
        visited[min_vertex] = True
        
        # Update distances to neighbors
        for v in range(num_vertices):
            weight = adj_matrix[min_vertex][v]
            if weight > 0 and distances[min_vertex] + weight < distances[v]:
                distances[v] = distances[min_vertex] + weight

    return distances

# Using adjacency matrix
# Use inf for missing edges
adj_matrix = [
    [0, 3, 1, float('inf'), float('inf')],
    [float('inf'), 0, float('inf'), 5, float('inf')],
    [float('inf'), float('inf'), 0, 2, float('inf')],
    [float('inf'), float('inf'), float('inf'), 0, 4],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0]
]

source_vertex = 0  # Starting from vertex 0
distances = dijkstra(adj_matrix, source_vertex)
print(distances)
