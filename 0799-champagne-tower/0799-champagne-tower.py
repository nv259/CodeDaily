class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glass = [[0] * 101 for _ in range(101)] 
        glass[0][0] = poured

        for row in range(100):
            for col in range(row + 1):
                if glass[row][col] > 1.:
                    glass[row + 1][col] += (glass[row][col] - 1) / 2
                    glass[row + 1][col + 1] += (glass[row][col] - 1) / 2
        
        return min(glass[query_row][query_glass], 1.)