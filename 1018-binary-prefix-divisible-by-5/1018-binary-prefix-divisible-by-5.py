class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        prefix_sum = 0
        for bin in nums:
            prefix_sum = prefix_sum * 2 + bin
            ans.append(prefix_sum % 5 ==  0)

        return ans