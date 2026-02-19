class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        N = len(s)
        s = [int(c) for c in s]
        consecutive_occurence = [ [0, 0] for _ in range(N + 1) ] # Nx2
        consecutive_occurence[0][s[0]] = 1

        for i in range(1, N):
            consecutive_occurence[i][s[i]] = consecutive_occurence[i - 1][s[i]] + 1

            if consecutive_occurence[i][s[i]] <= consecutive_occurence[i - consecutive_occurence[i][s[i]]][1 - s[i]]:
                ans += 1
        
        return ans