class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        chars = {}
        i, j = 0, 0
        ans = 0

        while i < N:
            if j < N and s[j] not in chars:
                chars[s[j]] = True
                j += 1
            else:
                del chars[s[i]]
                i += 1
            
            ans = max(ans, j - i)
        
        return ans