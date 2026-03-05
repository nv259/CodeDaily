class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)
        alt_0 = [0] * N
        alt_1 = [1] * N
        for i in range(1, N, 2):
            alt_0[i] = 1
            alt_1[i] = 0
        
        return min(
            sum([abs(int(s[i]) - alt_0[i]) for i in range(N)]),
            sum([abs(int(s[i]) - alt_1[i]) for i in range(N)])
        )