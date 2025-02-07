import numpy as np


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.arr = [0 for _ in range(4*self.n + 1)]

    def set_value(self, id, l, r, idx, val):
        if idx < l or r < idx:
            return

        if l == r == idx:
            self.arr[id] = val
            return
        
        mid = (l + r) // 2
        self.set_value(id * 2, l, mid, idx, val)
        self.set_value(id * 2 + 1, mid + 1, r, idx, val)
        self.arr[id] = self.arr[id * 2] + self.arr[id * 2 + 1] 

    def get_sum(self, id, l, r, u, v):
        if v < l or r < u:
            return 0
        
        if u <= l and r <= v:
            return self.arr[id]

        mid = (l + r) // 2
        return (self.get_sum(id * 2, l, mid, u, v)
                + self.get_sum(id * 2 + 1, mid + 1, r, u, v))


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Compress color into range [0, n) or so
        def compress(arr) -> (List[int], int):
            sorted_arr = sorted(arr)
            val2idx = dict()

            idx = 0
            for val in sorted_arr:
                if val not in val2idx:
                    val2idx[val] = idx
                    idx += 1
            
            return [val2idx[val] for val in arr], idx

        queries = np.array(queries)
        queries[:, 0], num_balls_upper_bound = compress(queries[:, 0])
        queries[:, 1], num_colors_upper_bound = compress(queries[:, 1])

        # Initilize
        res = []
        tree = SegmentTree(num_colors_upper_bound)
        count_color = [0 for _ in range(num_colors_upper_bound + 1)]
        ball_color = [None for _ in range(num_balls_upper_bound + 1)] 

        for x, y in queries:
            # Retrieve previous color
            z = ball_color[x]

            # Clear previous color (z) of ball x if x is already colored
            if z is not None:
                count_color[z] -= 1
    
                # If color (z) is nowhere used, update its value with 0
                if count_color[z] == 0:
                    tree.set_value(1, 0, num_colors_upper_bound, z, 0)
    
            # Mark ball x with the color y
            ball_color[x] = y
            count_color[y] += 1

            # If color y is used for the first time, update its value with 1
            if count_color[y] == 1:
                tree.set_value(1, 0, num_colors_upper_bound, y, 1)
                    
            # Retrieve the sum in range [0, n)
            res.append(tree.get_sum(1, 0, num_colors_upper_bound, 0, num_colors_upper_bound))
        
        return res