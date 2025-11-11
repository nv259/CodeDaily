class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def counter(s):
            num_zeros = 0
            for c in s:
                if c == '0': num_zeros += 1
            return (num_zeros, len(s) - num_zeros)
        
        pairs = []
        for s in strs:
            pairs.append(counter(s))
        pairs.sort()
        print(pairs)

        M, N = m, n
        dp = [[0 for _ in range(n + 1)]
                for _ in range(m + 1)]
        ans = 0

        for i in range(len(pairs)):
            for m in range(M, -1, -1):
                for n in range(N, -1, -1):
                    if m < pairs[i][0] or n < pairs[i][1]: continue

                    dp[m][n] = max(
                        1 + dp[m - pairs[i][0]][n - pairs[i][1]],
                        dp[m][n]
                    )
                    ans = max(ans, dp[m][n])
        
        return ans