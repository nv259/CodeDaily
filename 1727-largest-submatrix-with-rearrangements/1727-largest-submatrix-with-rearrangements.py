class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        cons_ones = [0] * N
        ans = 0

        for i in range(M):
            for j in range(N):
                cons_ones[j] = (0 if matrix[i][j] == 0
                                else cons_ones[j] + 1)

            sorted_cons_ones = sorted(cons_ones, reverse=True) 
            min_cons_ones = float('inf')
            for j in range(N):
                min_cons_ones = min(min_cons_ones, sorted_cons_ones[j])
                ans = max(ans, (j + 1) * min_cons_ones)
        
        return ans