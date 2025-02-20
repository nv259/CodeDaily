class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def backtrack(num):
            if len(num) == len(nums):
                return num if num not in nums else None
            
            for bit in ('0', '1'):
                ans = backtrack(num + bit)
                if ans is not None:
                    return ans
            
            return None

        return backtrack("")
