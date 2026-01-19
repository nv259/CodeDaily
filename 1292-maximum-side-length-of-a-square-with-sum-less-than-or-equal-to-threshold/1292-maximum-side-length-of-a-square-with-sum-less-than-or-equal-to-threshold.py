class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M, N = len(mat), len(mat[0])
        mat_sum = [[0] * (N + 1) for _ in range(M + 1)]  
        ans = 0 
        
        # Init 2D accumulative sum
        for i in range(M):
            for j in range(N):
                mat_sum[i][j] = (
                    mat_sum[i - 1][j] + mat_sum[i][j - 1] 
                    - mat_sum[i - 1][j - 1]
                    + mat[i][j]
                )

        for i in range(M):
            for j in range(N):
                # for each side-length
                for k in range(ans + 1, min(i, j) + 2):
                    square_sum = (
                        mat_sum[i][j] 
                        - mat_sum[i - k][j] - mat_sum[i][j - k]
                        + mat_sum[i - k][j - k]
                    ) 

                    if square_sum <= threshold:
                        ans = k
        
        return ans