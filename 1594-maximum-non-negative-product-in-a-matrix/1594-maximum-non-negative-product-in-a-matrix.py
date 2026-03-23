class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MODULO = int(1e9) + 7
        M, N = len(grid), len(grid[0])
        dp = [[[0, 0] for j in range(N)] for i in range(M)]

        dp[0][0] = [grid[0][0], grid[0][0]]
        for i in range(1, M): 
            dp[i][0] = [dp[i - 1][0][0] * grid[i][0], dp[i - 1][0][0] * grid[i][0]]
        for j in range(1, N): 
            dp[0][j] = [dp[0][j - 1][0] * grid[0][j], dp[0][j - 1][0] * grid[0][j]]

        for i in range(1, M):
            for j in range(1, N):
                max_ = max(dp[i - 1][j][0], dp[i - 1][j][1],
                            dp[i][j - 1][0], dp[i][j - 1][1])
                min_ = min(dp[i - 1][j][0], dp[i - 1][j][1],
                            dp[i][j - 1][0], dp[i][j - 1][1])
                dp[i][j][0] = max(max_ * grid[i][j], min_ * grid[i][j])
                dp[i][j][1] = min(max_ * grid[i][j], min_ * grid[i][j])
        
        return dp[-1][-1][0] % MODULO if dp[-1][-1][0] >= 0 else -1