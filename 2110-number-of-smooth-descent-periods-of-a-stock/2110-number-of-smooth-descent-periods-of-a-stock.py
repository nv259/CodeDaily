class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        def calc_number_of_segments(n):
            return n * (n + 1) // 2

        N = len(prices)
        i, j = 0, 0
        ans = 0
        prices.append(float('inf'))

        while j < N:
            if prices[j + 1] == prices[j] - 1:
                j += 1
            else:   # prices[j + 1] != prices[j] - 1
                ans += calc_number_of_segments(j - i + 1)
                j += 1
                i = j

        return ans