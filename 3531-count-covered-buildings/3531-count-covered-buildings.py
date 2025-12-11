class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings_x = {}    # x : ys
        buildings_y = {}    # y : xs
        for x, y in buildings:
            if x not in buildings_x:
                buildings_x[x] = []
            buildings_x[x].append(y)

            if y not in buildings_y:
                buildings_y[y] = []
            buildings_y[y].append(x)
        
        for x in buildings_x.keys():
            buildings_x[x].sort()
        for y in buildings_y.keys():
            buildings_y[y].sort()
        
        def is_covered(x, xs):
            i = bisect.bisect_left(xs, x)

            return 1 <= i < len(xs) - 1

        ans = 0
        for x, y in buildings:
            if (is_covered(y, buildings_x[x]) and 
                is_covered(x, buildings_y[y])):
                ans += 1
            
        return ans