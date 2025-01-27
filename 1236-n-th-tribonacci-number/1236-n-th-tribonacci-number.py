class Solution:
    def tribonacci(self, n: int) -> int:
        t = deque([0, 1, 1])
        if n < 3: return t[n]

        for i in range(3, n + 1):
            t_i = sum(t)
            t.popleft()
            t.append(t_i)
        
        return t_i

