class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def get_maximum_subarray(arr):
            total_sum = 0
            min_prefix_sum = float("inf")
            ans = 0

            for num in arr:
                total_sum += num
                ans = max(ans, total_sum - min_prefix_sum, total_sum)
                min_prefix_sum = min(min_prefix_sum, total_sum)

            return ans

        return max(get_maximum_subarray(nums),
                    get_maximum_subarray([-num for num in nums]),
                    0)
        