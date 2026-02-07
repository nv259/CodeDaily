class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()

        def bin_search(arr, key):
            # search for right-most idx : arr[idx] <= key
            ans = -1
            low, high = 0, len(arr) - 1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] <= key:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
                
            return ans
        
        ans = N
        for il, num in enumerate(nums):
            ir = bin_search(nums, num * k)
            # print(num, il, ir)
            ans = min(ans, il + N - ir - 1)
        
        return ans
