class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones_cnt = 0
        i = 0

        while i < len(s):
            if s[i] == '1':
                ones_cnt += 1
                i += 1
            else:
                while i < len(s) and s[i] == '0': i += 1
                ans += ones_cnt
        
        return ans