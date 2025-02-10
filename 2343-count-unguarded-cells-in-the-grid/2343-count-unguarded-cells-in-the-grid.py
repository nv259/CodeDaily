class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        is_guarded = [[False for _ in range(n)] 
                        for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        occupied_cells = sorted(guards + walls)
        print("Occupied cells:", occupied_cells) 
        for cell in occupied_cells:
            is_guarded[cell[0]][cell[1]] = True

        def exist(x, y):
            # Check for the presence of x in y
            i = bisect_left(y, x)
            if i == len(y): return False
            return y[i] == x
        
        def in_grid(x, y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x, y, curr_direction=None):
            if not in_grid(x, y):
                return -1

            # Mark this cell as guarded
            is_guarded[x][y] = True

            # If current cell is Guard or Wall then break
            # , given that current direction is not None
            if exist([x, y], occupied_cells) and curr_direction is not None:
                return 0

            # If current direction is None, i.e., we are 
            # checking a cell of Guard, check 4 directions 
            # of this guard.
            if curr_direction is None:
                for direction in directions:
                    dfs(x + direction[0], y + direction[1], direction)
            else: # Otherwise, keep shifting along current direction
                xm = x + curr_direction[0]
                ym = y + curr_direction[1]
                
                dfs(x + curr_direction[0], y + curr_direction[1], curr_direction)

            return 1

        for guard in guards:
            print(dfs(*guard))

        print("Grid", is_guarded)

        res = 0
        for i in range(m):
            for j in range(n): 
                res += (is_guarded[i][j] == False)

        return res
