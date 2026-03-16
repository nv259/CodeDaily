class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])

        # Check whether all 4 points are in grid, clockwise
        def is_valid(i, j, k):
            if not (0 <= i < M and 0 <= j < N): return False
            if not (0 <= i + k < M and 0 <= j + k < N): return False
            if not (0 <= i + 2 * k < M and 0 <= j < N): return False
            if not (0 <= i + k < M and 0 <= j - k < N): return False
            return True

        # sum[i][j][k] : accum sum from (i, j) to (i + k, j + k), inclusively
        def calc_diagonal_sum(grid):
            M, N = len(grid), len(grid[0])
            ans = [[[0 for k in range(min(M, N) + 1)]
                    for j in range(N)]
                    for i in range(M)]
            for i in range(M):
                for j in range(N):
                    for k in range(min(M, N)):
                        if not (0 <= i + k < M and 0 <= j + k < N): 
                            break
                        else:
                            # print(i, j, k, '\t', grid[i + k][j + k])
                            ans[i][j][k] = ans[i][j][k - 1] + grid[i + k][j + k]
            
            return ans

        # Calculate accumulative sum according to diagonals
        main_diag_sum = calc_diagonal_sum(grid)
        # Flip grid
        for i in range(M): grid[i] = grid[i][::-1]
        aux_diag_sum = calc_diagonal_sum(grid)
        for i in range(M): aux_diag_sum[i] = aux_diag_sum[i][::-1]
        for i in range(M): grid[i] = grid[i][::-1]
        # print(main_diag_sum)
        # print(aux_diag_sum)

        ans = [grid[i][j] for i in range(M) for j in range(N)]
        for i in range(M):
            for j in range(N):
                k = 1
                while True:
                    if not is_valid(i, j, k):
                        break
                    else:
                        ans.append(
                            main_diag_sum[i][j][k] - grid[i][j] + 
                            main_diag_sum[i + k][j - k][k] - grid[i + k][j + k] +
                            aux_diag_sum[i][j][k] - grid[i + 2*k][j] + 
                            aux_diag_sum[i + k][j + k][k] - grid[i + k][j - k]
                        )
                    k += 1

        return sorted(list(set(ans)), reverse=True)[:3]
        