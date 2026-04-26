class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])
        is_visit = [[False for j in range(N)]
                            for i in range(M)]

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j, local_visit):
            is_visit[i][j] = True

            for di, dj in d:
                next_idx_flatten = flatten_id(i + di, j + dj)
                if is_available(i + di, j + dj, grid[i][j]):
                    if is_visit[i + di][j + dj]: 
                        # print('check', i, j, i + di, j + dj)
                        if (next_idx_flatten in local_visit and 
                            len(local_visit) - local_visit[next_idx_flatten] >= 4):
                            return True
                        else: continue
                    else:
                        local_visit[next_idx_flatten] = len(local_visit)
                        exist_cycle = dfs(i + di, j + dj, local_visit)
                        del local_visit[next_idx_flatten]
                        if exist_cycle: return True
            
            return False

        def is_available(i, j, c):
            return 0 <= i < M and 0 <= j < N and grid[i][j] == c

        def flatten_id(i, j):
            return i * N + j
        
        for i in range(M):
            for j in range(N):
                if not is_visit[i][j]:
                    if dfs(i, j, {flatten_id(i, j): 0}):
                        return True
                    else: continue
                    
        return False
    