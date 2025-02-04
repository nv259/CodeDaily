class Graph: 
    def __init__(self, n):
        self.num_nodes = n
        self.adjacency = {}
 
        for u in range(self.num_nodes - 1):
            self.add_edge(u, u + 1, 1)
    
    def add_edge(self, u, v, w):
        if u not in self.adjacency:
            self.adjacency[u] = []

        self.adjacency[u].append([v, w])

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        city_graph = Graph(n)

        def shortest_path_length(graph, source, dest):
            def dijkstra(graph, source, dest):
                """ Calculate the shortest path from source to all node in the graph"""
                dist = [float("inf") for _ in range(graph.num_nodes)]   
                dist[source] = 0

                # Prepare priority queue
                pq = []
                heapq.heappush(pq, [0, source]) 

                while pq:
                    dist_u, u = heapq.heappop(pq)
                    
                    if u not in graph.adjacency: continue

                    for v, dist_uv in graph.adjacency[u]:
                        if dist[v] > dist_u + dist_uv:
                            dist[v] = dist_u + dist_uv
                            heapq.heappush(pq, [dist[v], v])

                return dist

            dist = dijkstra(graph, source, dest)
            return dist[dest]

        res = [] 
        for query in queries:
            city_graph.add_edge(query[0], query[1], 1)
            res.append(shortest_path_length(city_graph, 0, n - 1))
        
        return res