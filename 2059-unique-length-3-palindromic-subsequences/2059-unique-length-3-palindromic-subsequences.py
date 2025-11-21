class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        s = '@' + s
        N = len(s)
        # prefix_sum[c][i]: the total number of times
        # character `c` appears in s[0: i + 1] 
        prefix_sum = [[0 for _ in range(N)]
                      for _ in range(26)]
        for i, c in enumerate(s):
            if i == 0: continue

            for char_idx in range(26):
                prefix_sum[char_idx][i] = prefix_sum[char_idx][i - 1]
            char_idx = ord(c) - ord('a')
            prefix_sum[char_idx][i] += 1


        def count_unique_chars(l, r):
            # If there isn't any gap between two intervals
            if r - l < 2: return 0

            # The total number of times character `c` appears
            # in s[i: j] is prefix_sum[c][j] - prefix_sum[c][i - 1]
            ans = 0
            for char_idx in range(26):
                ans += (prefix_sum[char_idx][r - 1] - prefix_sum[char_idx][l]) > 0
        
            return ans
            
    
        def find_first_appearance(s, reversed=False):
            # Record the first appearance for each character
            ans = {}
            indices = ([i for i in range(N)] if not reversed
                    else [i for i in range(N - 1, -1, -1)])

            for idx in indices:
                if s[idx] not in ans:
                    ans[s[idx]] = idx
            
            return ans


        first_location = find_first_appearance(s)
        last_location = find_first_appearance(s, reversed=True)
        
        ans = 0 
        for char in first_location.keys():
            ans += count_unique_chars(first_location[char], last_location[char])

        return ans