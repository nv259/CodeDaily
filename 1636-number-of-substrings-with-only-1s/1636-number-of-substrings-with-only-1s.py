class Solution:
    def numSub(self, s: str) -> int:
        def  num_ones_with_length(n):
            return n * (n + 1) // 2

        s += '0'
        N = len(s)
        modulo = int(1e9) + 7
        ans = 0
    
        l, r = 0, 0
        while r < N:
            # expand to the right if valid
            if s[r] == '1':
                r += 1
            else:   
                # compute the number of ones for this window
                ans += num_ones_with_length(r - l) % modulo
                
                # initialize a new window
                r += 1
                l = r

        return ans % modulo