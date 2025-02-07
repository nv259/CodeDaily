class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        min_abs_val = float("inf")
        neg_count = 0

        for row in matrix:
            for val in row:
                res += abs(val)
                if val < 0: 
                    neg_count += 1
                min_abs_val = min(min_abs_val, abs(val))

        if neg_count % 2 != 0:
            res -= 2 * min_abs_val

        return res