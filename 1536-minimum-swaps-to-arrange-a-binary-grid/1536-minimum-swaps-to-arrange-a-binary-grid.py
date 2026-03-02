class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        pos = [0 for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    pos[i] = j
        
        right_most_set = sorted(pos)
        for i in range(N): 
            if right_most_set[i] > i: return -1

        ans = 0
        for i in range(N):
            k = -1
            for j in range(i, N):
                if pos[j] <= i:
                    ans += j - i
                    k = j
                    break
            
            if k != -1:
                for j in range(k, i, -1):
                    pos[j], pos[j - 1] = pos[j - 1], pos[j]
            else:
                return -1
        
        return ans