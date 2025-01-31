class DSU:
    def __init__(self, total_size):
        self.total_size = total_size
        self.parent = [-1 for _ in range(self.total_size)]
        self.size = [0 for _ in range(self.total_size)]
    
    def make_set(self, u):
        self.parent[u] = u
        self.size[u] = 1
    
    def find_set(self, u):
        if self.parent[u] == u:
            return u

        self.parent[u] = self.find_set(self.parent[u])
        return self.parent[u]
    
    def union_sets(self, u, v):
        # Return overall size at the end of the process
        u = self.find_set(u)
        v = self.find_set(v)

        if u != v:
            # attach v to u (u: bigger tree)
            if self.size[u] < self.size[v]:
                u, v = v, u
            self.parent[v] = u
            self.size[u] += self.size[v] 
        
        return self.size[u]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def coord_to_index(x, y, n_cols):
            return n_cols * x + y 

        def in_grid(x, y, m, n=None):
            if n is None: n = m
            return 0 <= x < m and 0 <= y < n

        n = len(grid)
        res = 1
        base = DSU(n*n) 
        # deltas = ((0, 1), (0, -1), (1, 0), (-1, 0))
        deltas = [(0, -1), (-1, 0)]  # only contain necessary directions, as we travel from left->right and up->down.

        # Initialize base data
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    current_idx = coord_to_index(i, j, n)
                    base.make_set(current_idx)

                    for di, dj in deltas:
                        im = i + di
                        jm = j + dj

                        if in_grid(im, jm, n) and grid[im][jm]:
                            neighbor_idx = coord_to_index(im, jm, n)
                            # dsu.make_set(neighbor_idx)
                            res = max(res, base.union_sets(current_idx, neighbor_idx))

        deltas = deltas + [(0, 1), (1, 0)]    # add 2 more directions
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    # tmp = deepcopy(base)  # deepcopy leads to TLE
                    unique_sets = set()
                    current_idx = coord_to_index(i, j, n)
                    # tmp.make_set(current_idx)

                    for di, dj in deltas:
                        im = i + di
                        jm = j + dj

                        if in_grid(im, jm, n) and grid[im][jm]:
                            neighbor_idx = coord_to_index(im, jm, n)
                            unique_sets.add(base.find_set(neighbor_idx))
                            # res = max(res, tmp.union_sets(current_idx, neighbor_idx))

                    size_ = 1   # flipped 0 to 1
                    for set_ in unique_sets:
                        size_ += base.size[set_]
                    res = max(res, size_)

        return res
