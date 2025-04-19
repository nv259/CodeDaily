class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0

        for idx, num in enumerate(nums):
            il = bisect.bisect_left(nums, lower - num, idx + 1, len(nums))
            ir = bisect.bisect_right(nums, upper - num, idx + 1, len(nums))

            ans += ir - il

        return ans

