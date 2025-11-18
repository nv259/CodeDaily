class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ans = False
        i, N = 0, len(bits) 

        while i < N:
            if bits[i] == 1:
                ans = False
                i += 2
            else:
                ans = True
                i += 1
        
        return ans