class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocess string
        ss = ""
        for c in s.lower():
            if ((0 <= ord(c) - ord('a') <= ord('z') - ord('a'))
                or (0 <= ord(c) - ord('0') <= 9)):
                ss += c
        
        i, j = 0, len(ss) - 1
        while i < j:
            if ss[i] == ss[j]:
                i += 1
                j -= 1
            else:
                return False
    
        return True