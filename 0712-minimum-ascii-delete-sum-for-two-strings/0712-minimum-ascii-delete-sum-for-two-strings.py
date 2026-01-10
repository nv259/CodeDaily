class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        M, N = len(s1), len(s2)
        # dp[i][j] : max ascii sum of longest common subsequence 
        # at s1's i-th position and s2's j-th position
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        
        for i in range(M):
            for j in range(N):
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        s1_ascii_sum = sum(ord(c) for c in s1)
        s2_ascii_sum = sum(ord(c) for c in s2)
        
        return s1_ascii_sum + s2_ascii_sum - 2 * dp[M - 1][N - 1]