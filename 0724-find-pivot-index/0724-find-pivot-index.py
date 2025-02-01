class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        def get_prefix_sum(arr):
            prefix_sum = [0 for _ in range(len(arr))]

            for i in range(1, len(arr)):
                prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

            return prefix_sum

        prefix_sum = get_prefix_sum(nums)
        suffix_sum = get_prefix_sum(nums[::-1])[::-1]

        for i in range(len(nums)):
            if prefix_sum[i] == suffix_sum[i]:
                return i
        
        return -1