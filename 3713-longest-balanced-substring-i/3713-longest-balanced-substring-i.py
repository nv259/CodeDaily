class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        freq = [[0] * (N + 1) for _ in range(27)]
        for i in range(N):
            for c in range(26):
                freq[c][i] = freq[c][i - 1]
            freq[ord(s[i]) - ord('a')][i] += 1

        def all_equal(arr):
            last = arr[0]
            for i in range(1, len(arr)):
                if arr[i] == 0: continue
                if last == 0: last = arr[i]
                if arr[i] != last:
                    return False
                last = arr[i]
            
            return True
         
        ans = 1
        for i in range(N):
            for j in range(0, i - ans + 1):
                if all_equal([freq[c][i] - freq[c][j - 1] for c in range(26)]):
                    ans = max(ans, i - j + 1)
        
        return ans
