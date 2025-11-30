class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        prefix_sum = [0] * N
        for i, num in enumerate(nums):
            prefix_sum[i] = (prefix_sum[i - 1] + num) % p
        arr_remain = prefix_sum[-1] % p

        if arr_remain == 0: return 0

        modulo_index = {0: -1}
        ans = N
        for i, prefix_sum_i in enumerate(prefix_sum):
            prefix_sum_j = (prefix_sum_i - arr_remain + p) % p
            if prefix_sum_j in modulo_index:
                ans = min(ans, i - modulo_index[prefix_sum_j])
            modulo_index[prefix_sum_i] = i

        return ans if ans != N else -1