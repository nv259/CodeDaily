class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dict_x = {}
        dict_y = {}
        # grid_type 0: free, 1: guard, -1: wall
        grid_type = [[0] * (n + 2) for _ in range(m + 2)]

        def record_dict(dict_x, dict_y, x, y):
            # Create a dictionary recording every occurred grid, sorted by y
            # quick accessment by x
            if x not in dict_y:
                dict_y[x] = [0, n + 1]
            dict_y[x].append(y)

            # Create a dictionary recording every occurred grid, sorted by y
            # quick accessment by x
            if y not in dict_x:
                dict_x[y] = [0, m + 1]
            dict_x[y].append(x)

            # return dict_x, dict_y

        for x, y in guards:
            x += 1
            y += 1
            record_dict(dict_x, dict_y, x, y)
            # Record the type
            grid_type[x][y] = 1

        for x, y in walls:
            x += 1
            y += 1
            record_dict(dict_x, dict_y, x, y)
            # Record the type
            grid_type[x][y] = -1
        
        for x in dict_y:
            dict_y[x].append(n + 1)
            dict_y[x].sort()
        for y in dict_x:
            dict_x[y].append(m + 1)
            dict_x[y].sort()


        def binary_search(arr, key):
            pos = bisect.bisect_left(arr, key)
            return arr[pos - 1], arr[pos]


        ans = 0
        for x in range(1, m + 1):
            for y in range(1, n + 1):
                if grid_type[x][y] == 0:
                    # print(x, y)
                    is_unguarded_horizontally = 1
                    if x in dict_y:
                        y_left, y_right = binary_search(dict_y[x], y)
                        # print('y', y_left, y_right, end=" ")

                        if grid_type[x][y_left] != 1 and grid_type[x][y_right] != 1:
                            is_unguarded_horizontally = 1
                        else: 
                            is_unguarded_horizontally = 0
                        # print(is_unguarded_horizontally)

                    is_unguarded_vertically = 1
                    if y in dict_x:
                        x_left, x_right = binary_search(dict_x[y], x)
                        # print('x', x_left, x_right, end=" ")

                        if grid_type[x_left][y] != 1 and grid_type[x_right][y] != 1:
                            is_unguarded_vertically = 1
                        else: 
                            is_unguarded_vertically = 0
                        # print(is_unguarded_vertically)

                    ans += is_unguarded_horizontally * is_unguarded_vertically
                    # print(ans)
        
        return ans


        