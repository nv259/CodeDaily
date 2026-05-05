class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        In a 90 degrees rotation, 
            (row, col) -> (col, n - 1 - row)
        <=>
            (row, col) --transpose--> (col, row) --reverse--> (col, n - 1 - row)
        """
        N = len(matrix)

        # Transpose: (row, col) <=> (col, row)
        for row in range(N):
            for col in range(row, N):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row], matrix[row][col]
                )
        
        # Reverse: (row, col[0;N - 1;1)) <=> (row, col(N - 1;0;-1))
        for row in range(N):
            for col in range(N // 2):
                matrix[row][col], matrix[row][N - 1 - col] = (
                    matrix[row][N - 1 - col], matrix[row][col]
                )

        return


