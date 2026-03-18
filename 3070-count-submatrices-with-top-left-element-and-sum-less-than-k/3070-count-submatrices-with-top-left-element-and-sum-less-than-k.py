class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        ans = 0

        for i in range(M):
            for j in range(N):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + grid[i][j]
                ans += dp[i][j] <= k
        
        return ans