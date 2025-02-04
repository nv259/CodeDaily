class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        window_sum = 0

        while r < len(nums):
            if l == r or nums[r - 1] < nums[r]:
                window_sum += nums[r]
                r += 1
            else:
                res = max(res, window_sum)
                l = r
                window_sum = 0
 
        return max(res, window_sum)