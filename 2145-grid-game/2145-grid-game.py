class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0

        res = float("inf")
        for j in range(len(grid[0])):
            first_row_sum -= grid[0][j]
            res = min(res, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][j]

        return res