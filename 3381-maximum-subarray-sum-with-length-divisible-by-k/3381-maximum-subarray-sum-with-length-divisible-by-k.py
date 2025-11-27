class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # prepend placeholder 0
        nums = [0] + nums
        N = len(nums)

        def calc_prefix_sum(arr):
            ans = [0] * N
            for i in range(N):
                ans[i] = ans[i - 1] + arr[i]
            return ans
        
        prefix_sum = calc_prefix_sum(nums)
        ans = -float("inf")
        minimum_prefix_sum = [ele for ele in prefix_sum[:k]]

        for i in range(k, N):
            type_ = i % k
            max_subarr_sum = prefix_sum[i] - minimum_prefix_sum[type_]
            ans = max(ans, max_subarr_sum)
            minimum_prefix_sum[type_] = min(minimum_prefix_sum[type_], prefix_sum[i])

        return ans



