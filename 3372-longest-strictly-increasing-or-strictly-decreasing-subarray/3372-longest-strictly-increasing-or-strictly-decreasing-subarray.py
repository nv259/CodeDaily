class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def find_longest_increasing_subarray(arr):
            res = 1
            l, r = 0, 0

            while r < len(arr):
                if l == r or arr[r] > arr[r - 1]:
                    r += 1
                else:
                    res = max(res, r - l)
                    l = r

            if r != l: res = max(res, r - l)

            return res

        return max(find_longest_increasing_subarray(nums),
                    find_longest_increasing_subarray([-num for num in nums]))