class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Convert edges list to adjacent list
        adj_list = [[] for _ in range(n)]
        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, 2 * w))

        d = [float('inf')] * n
        d[0] = 0
        pq = [(0, 0)]
        while len(pq):
            du, u = heapq.heappop(pq)
            
            if u == n - 1: return du

            for v, w_uv in adj_list[u]:
                if d[v] > du + w_uv:
                    d[v] = du + w_uv
                    heapq.heappush(pq, (d[v], v))

        return -1 if d[n - 1] == float('inf') else d[n - 1]