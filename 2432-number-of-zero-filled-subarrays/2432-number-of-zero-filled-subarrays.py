class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        left, right = 0, 0

        while left < len(nums):
            if nums[left] == 0:
                # find longest 0s subarray
                right = left
                while right < len(nums) and nums[right] == 0:
                    right += 1

                # calculate 
                num_elts = right - left
                res += num_elts * (num_elts + 1) // 2
                
                # quick update left position
                left = right
                
            # scan until left pivot equals 0
            left += 1

        return res

