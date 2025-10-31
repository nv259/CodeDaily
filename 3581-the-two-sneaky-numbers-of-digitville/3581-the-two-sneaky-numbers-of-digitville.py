class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_dict = {}
        ans = []
        for num in nums:
            if num in num_dict:
                ans.append(num)
            else:
                num_dict[num] = 1
        
        return ans