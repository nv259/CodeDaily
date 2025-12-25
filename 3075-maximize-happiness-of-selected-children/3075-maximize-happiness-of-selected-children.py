class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        cnt = 0
        for val in reversed(happiness[-k:]):
            ans += max(val - cnt, 0)
            cnt += 1
        return ans