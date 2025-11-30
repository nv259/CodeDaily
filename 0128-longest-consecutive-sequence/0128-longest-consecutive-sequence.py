class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        avail = {}
        for num in nums:
            avail[num] = True
        
        def traverse(num, direction):
            if num not in avail or not avail[num]:
                return 0
            
            avail[num] = False
            return traverse(num + direction, direction) + 1
       
        ans = 0 
        for num in nums:
            if num in avail:
                ans = max(ans, traverse(num + 1, 1) + traverse(num - 1, -1) + 1)
                avail[num] = False
        
        return ans 