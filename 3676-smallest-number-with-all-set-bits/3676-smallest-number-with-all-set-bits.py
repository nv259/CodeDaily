class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 0
        val_bit = 1
        while n:
            n //= 2
            ans += val_bit
            val_bit *= 2

        return ans

