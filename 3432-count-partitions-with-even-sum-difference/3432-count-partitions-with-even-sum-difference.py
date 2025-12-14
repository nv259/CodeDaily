class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums) 
        prefix_sum = 0
        ans = 0

        for num in nums[:-1]:
            prefix_sum += num
            if abs(total_sum - 2 * prefix_sum) % 2 == 0:
                ans += 1
        
        return ans
         