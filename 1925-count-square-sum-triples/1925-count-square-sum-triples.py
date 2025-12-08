class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n):
            for b in range(a, n):
                c2 = a ** 2 + b ** 2
                c = int(c2 ** 0.5)
                if c > n: break
                if c ** 2 == c2:
                    cnt += 2
        
        return cnt