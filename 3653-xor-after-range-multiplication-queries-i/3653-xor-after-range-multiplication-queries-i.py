class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MODULO = int(1e9) + 7

        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MODULO
                idx += k

        ans = nums[0]
        for num in nums[1:]:
            ans = ans ^ num

        return ans