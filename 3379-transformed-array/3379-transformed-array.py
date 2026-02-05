class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        for idx, num in enumerate(nums):
            m_idx = (num + idx) % len(nums)
            result.append(nums[m_idx])
        
        return result
