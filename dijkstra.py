import heapq

def dijkstra(graph, start):
    n = len(graph)
    distance = [float('inf')] * n
    distance[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distance[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distance


# ---------------- Main Program ----------------

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = [[] for _ in range(vertices)]

print("Enter each edge (source destination weight):")

for _ in range(edges):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))   # Remove this line for directed graph

source = int(input("Enter source vertex: "))

distances = dijkstra(graph, source)

print("\nShortest distances from source vertex", source)

for vertex, distance in enumerate(distances):
    print(f"Vertex {vertex}: {distance}")