class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for _ in range(numRows - 1):
            tmp = [1]
            for idx in range(len(res[-1]) - 1):
                tmp.append(res[-1][idx] + res[-1][idx + 1])
            tmp.append(1)

            res.append(tmp)
        
        return res

