class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        N = len(bottomLeft)

        def calc_intersect_hw(
            x_low_1, y_low_1,
            x_high_1, y_high_1,
            x_low_2, y_low_2,
            x_high_2, y_high_2,
        ):
            h = min(y_high_1, y_high_2) - max(y_low_1, y_low_2)
            w = min(x_high_1, x_high_2) - max(x_low_1, x_low_2)

            return (h, w) if (h > 0 and w > 0) else (0, 0)

        ans = 0
        for i in range(1, N):
            for j in range(i):
                if i == j: continue

                h, w = calc_intersect_hw(
                    bottomLeft[i][0], bottomLeft[i][1], 
                    topRight[i][0], topRight[i][1],
                    bottomLeft[j][0], bottomLeft[j][1], 
                    topRight[j][0], topRight[j][1],
                )
                
                ans = max(ans, min(h, w)**2)
            
        return ans