class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Count number of distinct elements in the whole array
        n = len(nums)
        arr_cnt = len(set(nums))
        ret = 0

        for i in range(n):
            tmp = {}
            cnt = 0
            for j in range(i, n):
                if nums[j] not in tmp:
                    tmp[nums[j]] = True
                    cnt += 1

                if cnt == arr_cnt:
                    ret += 1

        return ret
