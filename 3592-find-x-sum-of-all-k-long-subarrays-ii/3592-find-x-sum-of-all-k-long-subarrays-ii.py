from sortedcontainers import SortedList
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        n = len(nums)
        
        # Initialize the sliding window
        window = Counter(nums[:k])  # num : occur
        for num in nums:
            window[num] += 0 

        sl = SortedList()           # occur : num
        for num, occur in window.items():
            sl.add((occur, num))

        total_sum = 0
        for occur, num in sl[-x:]:
            total_sum += occur * num
        ans.append(total_sum)

        def update(total_sum, sl, num, delta):
            # Retrieve `num`
            idx = sl.bisect_left((window[num], num))
            # If to-be-updated num is in top-x
            if idx >= len(sl) - x:
                # Remove from total_sum
                # total_sum -= sl[idx][0] * sl[idx][1]
                total_sum -= window[num] * num
                # Include top-(x + 1) from total_sum 
                if len(sl) - x > 0:
                    total_sum += sl[len(sl) - x - 1][0] * sl[len(sl) - x - 1][1]
            sl.remove((window[num], num))

            # Update num occurences
            window[num] += delta

            # Find the rank of the updated num
            sl.add((window[num], num))
            idx = sl.bisect_left((window[num], num))
            # If it's in top-x
            if idx >= len(sl) - x:
                # Include the updated num in total_sum
                total_sum += window[num] * num
                # Remove top-(x + 1) from total_sum (previously, top-x)
                if len(sl) - x > 0:
                    total_sum -= sl[len(sl) - x - 1][0] * sl[len(sl) - x - 1][1]

            return total_sum


        # Slide the window to the right
        for i in range(k, n):
            total_sum = update(total_sum, sl, nums[i], 1)
            total_sum = update(total_sum, sl, nums[i - k], -1)
            ans.append(total_sum)
        
        return ans 