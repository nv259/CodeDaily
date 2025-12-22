class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        strs[0][0] strs[0][1] ... strs[0][M - 1]
        strs[1][0] strs[1][1] ... strs[1][M - 1]
        (N - 1)
        ---
        strs[N][0] strs[N][1] ... strs[N][M - 1]
        """
        N = len(strs)
        M = len(strs[0])
        dp = [1] * M

        for j in range(1, M):
            for prev_j in range(j):
                check = all(strs[i][prev_j] <= strs[i][j] for i in range(N))
                if check:
                    dp[j] = max(dp[j], dp[prev_j] + 1)

        return M - max(dp) 
