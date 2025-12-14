class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        modulo = int(1e9) + 7
        N = len(nums)
        counter = Counter(nums)
        for i in range(N):
            nums[i] = (nums[i], i)
        nums.sort()
        nums.append((float('inf'), float('inf')))
        
        def bisect_left(arr, num, idx):
            low, high = 0, len(arr) - 1
            ans = high

            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid][0] < num:
                    low = mid + 1
                elif arr[mid][0] > num:
                    high = mid - 1
                elif arr[mid][0] == num:
                    if arr[mid][1] < idx:
                        ans = mid
                        low = mid + 1
                    elif arr[mid][1] >= idx:
                        high = mid - 1

            return ans 
        
        def bisect_right(arr, num, idx):
            low, high = 0, len(arr) - 1 
            ans = high

            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid][0] < num:
                    low = mid + 1
                elif arr[mid][0] > num:
                    high = mid - 1
                elif arr[mid][0] == num:
                    if arr[mid][1] > idx:
                        ans = mid
                        high = mid - 1
                    else:
                        low = mid + 1

            return ans 

        def left_most(arr, num):
            low, high = 0, len(arr) - 1
            ans = high

            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid][0] >= num:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            return ans 
        
        def right_most(arr, num):
            low, high = 0, len(arr) - 1
            ans = high

            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid][0] <= num:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            return ans 
        
        
        ans = 0
        for num, idx in nums:
            if counter[num * 2] < 2:
                continue
            
            lm = left_most(nums, num * 2)
            bl = bisect_left(nums, num * 2, idx)
            if nums[bl][0] != num * 2 or nums[bl][1] >= idx:
                continue
            rm = right_most(nums, num * 2)
            br = bisect_right(nums, num * 2, idx)
            if nums[br][0] != num * 2 or nums[br][1] <= idx:
                continue

            ans = (ans + (bl - lm + 1) * (rm - br + 1) % modulo) % modulo
        
        return ans