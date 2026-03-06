class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        N = len(s)
        i = 0
        counter_zero = False

        while i < N:
            for j in range(i, N):
                if s[j] == '0':
                    counter_zero = True
                    break
                elif s[j] == '1' and counter_zero:
                    return False
            
            i = j + 1
            
        return True