class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs)
        M = len(strs[0])
        ans = 0
        
        for col in range(M):
            for row in range(1, N):
                if strs[row][col] < strs[row - 1][col]:
                    ans += 1
                    break
        
        return ans