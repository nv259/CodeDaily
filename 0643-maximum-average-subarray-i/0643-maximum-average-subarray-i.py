class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize window from 0 to k
        window_sum, l = 0, 0
        for r in range(k):
            window_sum += nums[r]
        max_sum = window_sum

        for r in range(k, len(nums)):
            window_sum += nums[r] - nums[l]
            max_sum = max(max_sum, window_sum)

            l += 1

        return max_sum / k