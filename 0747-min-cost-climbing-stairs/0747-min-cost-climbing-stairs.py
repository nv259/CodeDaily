class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f = [float('inf')] * (len(cost) + 1)
        f[0], f[1] = 0, 0

        for floor in range(2, len(cost) + 1):
            f[floor] = min(
                f[floor - 1] + cost[floor - 1],
                f[floor - 2] + cost[floor - 2]
            )

        return f[len(cost)]