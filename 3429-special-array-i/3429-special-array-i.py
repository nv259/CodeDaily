class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        nums = [num % 2 for num in nums]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return False

        return True            
            
