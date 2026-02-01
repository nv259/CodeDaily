class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        nums = sorted(nums[1:])
        return cost + nums[0] + nums[1]