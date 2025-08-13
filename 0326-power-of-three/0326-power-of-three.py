class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False

        # n == 3^x
        # ln(n) == x ln(3)
        # x = ln(n) / ln(3)
        x = round(math.log(n) / math.log(3))
        
        return 3**x == n