class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj = {}
        self.create_self_loop()
        
    def create_self_loop(self):
        for node in range(self.num_nodes):
            self.adj[node] = [(node, 0)]

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def in_grid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def convert_to_graph(grid):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            graph = Graph(len(grid) * len(grid[0]))

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    curr_idx = i * len(grid[0]) + j

                    for di, dj in directions:
                        new_i = i + di
                        new_j = j + dj

                        if in_grid(new_i, new_j):
                            graph.add_edge(
                                curr_idx,
                                new_i * len(grid[0]) + new_j, 
                                grid[i][j]
                            )

            
            return graph

        def dijkstra(graph, source, dest):
            dist = [float('inf')] * graph.num_nodes
            dist[source] = 0
            pq = [(0, source)]

            while pq:
                dist_u, u = heapq.heappop(pq)

                for v, w_uv in graph.adj[u]:
                    if dist[v] > dist_u + w_uv:
                        dist[v] = dist_u + w_uv
                        heapq.heappush(pq, (dist[v], v)) 
                        
            return dist[dest]

        graph = convert_to_graph(grid)
        print(graph.num_nodes   )
        return dijkstra(graph, 0, len(grid)*len(grid[0]) - 1)