class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0 for _ in range(n)]
        for u, v in edges:
            in_degree[v] += 1

        champion = -1
        for team in range(n):
            if in_degree[team] == 0:
                if champion == -1:
                    champion = team
                else: 
                    return -1

        return champion
            