class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # prefix[i] : prefix sum of [0, i)
        def calc_prefix_sum(arr):
            ans = [0] * len(arr)
            for idx in range(0, len(arr) - 1):
                ans[idx + 1] = ans[idx] + arr[idx]
            return ans

        prefix_sum = calc_prefix_sum(nums)
        suffix_sum = calc_prefix_sum(nums[::-1])[::-1]
        ans = 0

        for idx, num in enumerate(nums):
            if num == 0:
                if prefix_sum[idx] == suffix_sum[idx]:
                    ans += 2
                elif prefix_sum[idx] + 1 == suffix_sum[idx]:
                    ans += 1
                elif prefix_sum[idx] == suffix_sum[idx] + 1:
                    ans += 1
        
        return ans

