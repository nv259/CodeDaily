class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        sum_row = [0] * M
        sum_col = [0] * N

        for i in range(M):
            for j in range(N):
                sum_row[i] += mat[i][j] 
                sum_col[j] += mat[i][j]
        
        return sum(sum_row[i] == 1 and sum_col[j] == 1 and mat[i][j] == 1
                    for i in range(M)
                    for j in range(N))