class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        ans = 0

        for idx in range(1, N):
            diff = (abs(points[idx][0] - points[idx - 1][0]),
                    abs(points[idx][1] - points[idx - 1][1]))
            ans += min(diff) + max(diff) - min(diff)

        return ans