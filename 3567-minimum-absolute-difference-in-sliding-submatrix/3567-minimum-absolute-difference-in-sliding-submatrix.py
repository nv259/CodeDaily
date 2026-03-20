class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        ans = []

        for i in range(M - k + 1):
            ans_row = []
            for j in range(N - k + 1):
                sl = []
                for ik in range(i, i + k):
                    for jk in range(j, j + k):
                        sl.append(grid[ik][jk])

                sl = sorted(list(set(sl)))

                ans_row.append(
                    0 if len(sl) == 1 else
                    min(abs(sl[k] - sl[k - 1]) for k in range(1, len(sl)))
                )

            ans.append(ans_row)
        
        return ans
