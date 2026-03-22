class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def are_equal(grid1, grid2):
            N = len(grid1)
            for i in range(N):
                for j in range(N):
                    if grid1[i][j] != grid2[i][j]:
                        return False
            
            return True

        def rotate_right(grid):
            N = len(grid)
            ans = [[0] * N for _ in range(N)]
            j = N - 1

            for i in range(N):
                for k in range(N):
                    ans[k][j] = grid[i][k]
                j -= 1

            return ans

        for _ in range(4):
            mat = rotate_right(mat)
            if are_equal(mat, target):
                return True

        return False