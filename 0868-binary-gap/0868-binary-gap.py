class Solution:
    def binaryGap(self, n: int) -> int:
        def to_bit(n):
            ans = []
            one_cnt = 0

            while n: 
                ans.append(n % 2)
                one_cnt += n % 2
                n //= 2
            
            return ans, one_cnt

        ans, prev = 0, None
        n, one_cnt = to_bit(n)
        if one_cnt < 2: return 0

        for idx, bit in enumerate(n):
            if bit == 1:
                if prev is not None:
                    ans = max(ans, idx - prev)
                prev = idx
            
        return ans
