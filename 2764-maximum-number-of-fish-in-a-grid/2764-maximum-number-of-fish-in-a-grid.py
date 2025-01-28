class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # Metadata
        m, n = len(grid), len(grid[0])
        res = 0

        # Mark all lands as cannot be fished (ofc!)
        can_fish = [[True for _ in range(n)]
                        for _ in range(m)]
        for row in range(m):
            for col in range(n):
                can_fish[row][col] = (grid[row][col] != 0)

        def in_grid(row, col):
            return 0 <= row < m and 0 <= col < n

        # Define directions for moving
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(row, col):
            total_fish = 0
            queue = deque([(row, col)])
            can_fish[row][col] = False

            while queue:
                row, col = queue.popleft()
                total_fish += grid[row][col]
            
                # Move to adjacent water cells
                for d_row, d_col in delta:
                    if (in_grid(row + d_row, col + d_col)
                        and can_fish[row + d_row][col + d_col]):
                        can_fish[row + d_row][col + d_col] = False
                        queue.append((row + d_row, col + d_col))

            return total_fish

        for row in range(m):
            for col in range(n):
                if can_fish[row][col] and grid[row][col]:
                    res = max(res, bfs(row, col))
        
        return res
        


        