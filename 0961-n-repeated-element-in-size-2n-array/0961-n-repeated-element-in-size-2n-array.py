class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                return num
        
        return -1