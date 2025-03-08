class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        il = 0
        res = float("inf")
        cnt_0 = 0

        for ir in range(len(blocks)):
            if blocks[ir] == 'W':
                cnt_0 += 1

            if ir == k - 1: res = cnt_0
            
            if ir >= k:
                if blocks[ir - k] == 'W':
                    cnt_0 -= 1
                res = min(res, cnt_0)

        return min(res, cnt_0)
