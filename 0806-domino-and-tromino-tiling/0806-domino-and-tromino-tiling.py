class Solution:
    def numTilings(self, n: int) -> int:
        f = [0] * max(4, n + 1)
        f[1], f[2], f[3] = 1, 2, 5
       
        if n <= 3: return f[n]

        for i in range(4, n + 1):
            f[i] = (2*f[i - 1] + f[i - 3]) % (int(1e9) + 7)
        
        return f[n]