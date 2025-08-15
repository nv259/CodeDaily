class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False

        # n == 4^x
        # ln(n) == x ln(4)
        # x = ln(n) / ln(4)
        x = round(math.log(n) / math.log(4))
        
        return 4**x == n
