class Solution:
    def check(self, nums: List[int]) -> bool:
        def is_not_decreasing(arr):
            if len(arr) in (0, 1): return True

            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False

            return True

        for i in range(len(nums)):
            if (is_not_decreasing(nums[:i]) and 
                is_not_decreasing(nums[i:])):
                if i == 0:
                    return True
                if i != 0 and nums[-1] <= nums[0]:
                    return True
                    

        return False