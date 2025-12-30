class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def is_magic_square(i, j):
            # 1 -> 9
            nums = [False] * 16
            for ii in range(i, i + 3):
                for jj in range(j, j + 3):
                    nums[grid[ii][jj]] = True
            
            if not all(nums[1: 10]):
                return 0

            # Row Sum
            sum_arr = []
            for ii in range(i, i + 3):
                sum_arr.append(grid[ii][j] + grid[ii][j + 1] + grid[ii][j + 2])

            if not (sum_arr[0] == sum_arr[1] == sum_arr[2]):
                return 0
            row_sum = sum_arr[0]

            # Col Sum
            sum_arr = []
            for jj in range(j, j + 3):
                sum_arr.append(grid[i][jj] + grid[i + 1][jj] + grid[i + 2][jj])
            
            if not (sum_arr[0] == sum_arr[1] and sum_arr[1] == sum_arr[2]):
                return 0
            col_sum = sum_arr[0]

            # Diag Sum
            main_diag_sum = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
            counter_diag_sum = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]

            return row_sum == col_sum == main_diag_sum == counter_diag_sum

        ans = 0
        for i in range(M - 2):
            for j in range(N - 2):
                if 1 <= grid[i][j] <= 9:
                    ans += is_magic_square(i, j)

        return ans

        
    