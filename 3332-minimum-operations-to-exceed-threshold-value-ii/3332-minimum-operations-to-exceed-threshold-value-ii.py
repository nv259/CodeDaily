class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0

        while nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, 2 * min(x, y) + max(x, y))
            
            res += 1
        
        return res
