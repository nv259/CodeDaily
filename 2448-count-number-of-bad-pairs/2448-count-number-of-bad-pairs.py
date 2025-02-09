class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res = 0
        index_value_diff = dict()

        for idx, num in enumerate(nums):
            diff = idx - num

            gud_pairs_cnt = index_value_diff.get(diff, 0)
            res += idx - gud_pairs_cnt

            index_value_diff[diff] = gud_pairs_cnt + 1

        return res