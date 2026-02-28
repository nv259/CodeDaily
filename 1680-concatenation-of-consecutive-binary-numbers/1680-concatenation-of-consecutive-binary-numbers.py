class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo = int(1e9) + 7
        def to_bin_len(n):
            ans = 0
            while n:
                ans += 1
                n //= 2
            
            return ans
        
        ans = 0
        for i in range(1, n + 1):
            ans = ((ans << to_bin_len(i)) % modulo + i) % modulo
        
        return ans % modulo