class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = int(high - low + 1) // 2
        if low % 2 == 1 and high % 2 == 1:
            return ans + 1
        return ans