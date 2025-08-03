class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, res = 0, 0
        remain_flip_cnt = k

        for j in range(len(nums)):
            if nums[j] == 0:
                if remain_flip_cnt > 0:
                    remain_flip_cnt -= 1
                else:
                    while i <= j and nums[i] == 1 and remain_flip_cnt < k:
                        i += 1
                    if k == 0: i = j

                    i += 1
            
            res = max(res, j - i + 1)

        return res 