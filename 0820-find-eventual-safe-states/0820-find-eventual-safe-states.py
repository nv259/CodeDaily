class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Initialize
        n = len(graph)
        safe_nodes = []
        queue = deque()

        # Transpose the graph
        transpose_graph = [[] for _ in range(n)]
        for node_idx, neighbors in enumerate(graph):
            for neighbor in neighbors:
                transpose_graph[neighbor].append(node_idx)

        # Kahn's algorithm 
        ## Count in-degree for each node
        in_degrees = [0 for _ in range(n)]
        for node_idx in range(n):
            in_degrees[node_idx] = len(graph[node_idx])
            if in_degrees[node_idx] == 0:
                queue.append(node_idx)

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)

            for neighbor in transpose_graph[node]:
                in_degrees[neighbor] -= 1

                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted(safe_nodes)