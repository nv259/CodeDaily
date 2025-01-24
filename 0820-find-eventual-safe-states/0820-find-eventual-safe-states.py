class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(u):
            if u in safe: 
                return safe[u]

            safe[u] = False

            for v in graph[u]:
                if not dfs(v):
                    return False
                
            safe[u] = True
            return True

        res = []

        for node in range(n):
            if dfs(node):
                res.append(node)

        return res