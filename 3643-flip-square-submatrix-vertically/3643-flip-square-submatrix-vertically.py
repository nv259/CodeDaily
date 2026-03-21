class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        i = x
        j = x + k - 1

        while i < j:
            grid[i][y : y + k], grid[j][y : y + k] = (
                grid[j][y : y + k], grid[i][y : y + k]
            )
            i += 1
            j -= 1
        
        return grid