class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(x, k):
            if x == 0: return True

            cnt = 0
            for pile in candies:
                cnt += pile // x
                if cnt >= k:
                    return True
            return False

        low, high = 0, sum(candies) // k
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if check(mid, k):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        
        return ans