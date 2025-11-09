class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])

        def in_grid(i, j):
            return 0 <= i < m and 0 <= j < n

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            grid[i][j] = '0'

            for di, dj in directions:
                mi = i + di
                mj = j + dj

                if in_grid(mi, mj) and grid[mi][mj] == '1':
                    dfs(mi, mj) 
            

        ans = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans

