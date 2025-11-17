class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        N = len(nums)

        for l in range(N):
            if nums[l] == 1: break
        r = l + 1

        while r < N:
            if nums[r] == 0:
                r += 1
            else:
                if r - l - 1 < k:
                    return False

                l = r
                r += 1

        return True
                
        