class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        source = [ord(source[i]) - ord('a') for i in range(len(source))]
        target = [ord(target[i]) - ord('a') for i in range(len(target))]
        original = [ord(original[i]) - ord('a') for i in range(len(original))]
        changed = [ord(changed[i]) - ord('a') for i in range(len(changed))]

        adj_list = [[] for _ in range(26)]
        for ori, cha, cos in zip(original, changed, cost):
            adj_list[ori].append((cha, cos)) 
    
        d = [[float('inf')] * 26 for _ in range(26)]
        def dijskstra(start):
            d[start][start] = 0
            pq = [(0, start)]

            while len(pq):
                du, u = heapq.heappop(pq)
                
                for v, d_uv in adj_list[u]:
                    if d[start][v] > du + d_uv:
                        d[start][v] = du + d_uv
                        heapq.heappush(pq, (d[start][v], v))
                
        for start in range(26): dijskstra(start) 

        ans = sum(d[source[i]][target[i]] for i in range(len(source)))
        return ans if ans != float('inf') else -1

