class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        M, N = len(mat), len(mat[0])
        if k % N == 0: return True

        def shift_right(row):
            tmp = row[-1]
            for j in range(len(row) - 1, -1, -1):
                row[j] = row[j - 1] 
            row[0] = tmp
        
        def shift_left(row):
            tmp = row[0]
            for j in range(0, len(row) - 1):
                row[j] = row[j + 1]
            row[-1] = tmp

        orig = copy.deepcopy(mat)

        # Simulate
        for k_ in range(k):
            # print(mat[1])
            for i in range(0, M, 2):
                shift_left(mat[i])
            for i in range(1, M, 2):
                shift_right(mat[i])
            # print('\t', mat[1])

        # print(orig)
        # print(mat)
        return orig == mat 
        