class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(N + 1)] for _ in range(M + 1)] 
        ans = 0

        for i in range(M):
            for j in range(N):
                for idx in [0, 1]:
                    dp[i][j][idx] = (
                        dp[i - 1][j][idx] + dp[i][j - 1][idx]
                        - dp[i - 1][j - 1][idx]
                    )

                if grid[i][j] != '.':
                    idx = "XY".index(grid[i][j])
                    dp[i][j][idx] += 1

                ans += (dp[i][j][0] == dp[i][j][1]) and (dp[i][j][0] > 0)

        return ans