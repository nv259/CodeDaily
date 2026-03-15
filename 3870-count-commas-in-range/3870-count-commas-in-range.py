class Solution:
    def countCommas(self, n: int) -> int:
        return sum(len(str(i)) // 4 for i in range(1, n + 1))