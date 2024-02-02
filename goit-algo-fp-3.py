import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))


def dijkstra(graph, start_vertex):
    D = [float('inf')] * graph.V
    D[start_vertex] = 0

    pq = [(0, start_vertex)]
    while pq:
        (dist, current_vertex) = heapq.heappop(pq)

        if dist > D[current_vertex]:
            continue

        for neighbor, weight in graph.graph[current_vertex]:
            distance = D[current_vertex] + weight
            if distance < D[neighbor]:
                D[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return D


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

start_vertex = 0
result = dijkstra(g, start_vertex)

print(result)
