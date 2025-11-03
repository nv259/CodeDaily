class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        max_retained_time = 0
        i = 0

        # loop over balloons
        while i < n:
            max_neededTime = neededTime[i]

            j = i + 1
            while j < n and colors[j] == colors[i]:
                max_neededTime = max(max_neededTime, neededTime[j])
                j += 1

            max_retained_time += max_neededTime
            i = j

        return sum(neededTime) - max_retained_time