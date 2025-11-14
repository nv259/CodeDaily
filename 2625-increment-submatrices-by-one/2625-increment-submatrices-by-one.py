class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for _ in range(n)]
                  for _ in range(n)] 

        for row1, col1, row2, col2 in queries:
            # increase matrix[row1: row2 + 1][col1]
            for row in range(row1, row2 + 1):
                matrix[row][col1] += 1

            if col2 + 1 >= n: continue
            # decrease matrix[row1: row2 + 1][col2 + 1]
            for row in range(row1, row2 + 1):
                matrix[row][col2 + 1] -= 1
            
        for i in range(n):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]

        return matrix 