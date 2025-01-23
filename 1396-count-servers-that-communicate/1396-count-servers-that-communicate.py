class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # grid = np.array(grid)
        desired_servers = set()
        n_rows, n_cols = len(grid), len(grid[0])

        for row_idx in range(n_rows):
            if sum(grid[row_idx]) > 1:
                for col_idx in range(n_cols):
                    if grid[row_idx][col_idx]:
                        desired_servers.add((row_idx, col_idx))

        for col_idx in range(n_cols):
            total_servers = 0
            for row_idx in range(n_rows):
                total_servers += grid[row_idx][col_idx]
            
            if total_servers > 1:
                for row_idx in range(n_rows):
                    if grid[row_idx][col_idx]:
                        desired_servers.add((row_idx, col_idx)) 

        return len(desired_servers)
