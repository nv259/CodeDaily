class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        num2ids = {}
        for idx, num in enumerate(nums):
            if num not in num2ids:
                num2ids[num] = []
            num2ids[num].append(idx)
        
        ans = float('inf')
        for num, ids in num2ids.items():
            if len(ids) >= 3:
                for i in range(0, len(ids) - 2):
                    ans = min(ans, 2 * (ids[i + 2] - ids[i]))
        
        return -1 if ans == float('inf') else ans