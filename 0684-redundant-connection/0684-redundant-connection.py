class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
    
    def make_set(self, u):
        self.parent[u] = u

    def find_set(self, u):
        return u if self.parent[u] == u else self.find_set(self.parent[u])
    
    def union_sets(self, u, v):
        x = self.find_set(u)
        y = self.find_set(v)

        if x != y: self.parent[y] = x

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        res = [0, 0]

        for u, v in edges:
            # 0-based index
            u = u - 1
            v = v - 1

            if dsu.find_set(u) == dsu.find_set(v):
                res = [u, v]

            dsu.union_sets(u, v)

        res[0] = res[0] + 1
        res[1] = res[1] + 1

        return res