class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Initialize variables
        m = len(mat)
        n = len(mat[0])
        val2idx = {}
        count_col = [0 for _ in range(n)]
        count_row = [0 for _ in range(m)]

        # Create hash table
        for row_idx in range(m):
            for col_idx in range(n):
                val2idx[mat[row_idx][col_idx]] = (row_idx, col_idx)

        # Paint the matrix
        for i in range(m*n):
            row_idx, col_idx = val2idx[arr[i]]

            count_col[col_idx] += 1
            count_row[row_idx] += 1

            if count_col[col_idx] == m or count_row[row_idx] == n:
                return i
        
        return m*n  # Just in case