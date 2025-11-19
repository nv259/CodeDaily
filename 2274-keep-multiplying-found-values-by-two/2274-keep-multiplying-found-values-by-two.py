class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        N = len(nums)
        nums.sort()

        def binary_search(nums, key, l, r):
            ans = -1
            exist = False
            
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] <= key:
                    if nums[mid] == key:
                        ans = mid
                        exist = True
                    l = mid + 1
                else:
                    r = mid - 1
            
            return ans, exist
        
        idx = -1 
        while True:
            idx, exist = binary_search(nums, original, idx + 1, N - 1)
            if exist:  
                original *= 2
            else:
                return original
            
