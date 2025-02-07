class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        decay_time = [[9999 for _ in range(n)]
                        for _ in range(m)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def in_grid(i, j):
            return (0 <= i < m) and (0 <= j < n)

        def dfs(i, j, time):
            decay_time[i][j] = time
            
            for di, dj in directions:
                im = i + di
                jm = j + dj

                if in_grid(im, jm) \
                    and grid[im][jm] == 1 \
                    and decay_time[im][jm] > time + 1:
                    dfs(im, jm, time + 1)

            return 0
        
        # DFS starting from rotten orange
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    decay_time[i][j] = 0
                    dfs(i, j, 0)
        print(decay_time)
        # Check all oranges.
        # If there exists one orange that cannot be rotten, 
        # i.e., decay_time is 9999, return impossible
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, decay_time[i][j])

        return -1 if res == 9999 else res
                