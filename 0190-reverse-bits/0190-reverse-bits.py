class Solution:
    def reverseBits(self, n: int) -> int:
        def int2reversed_bit(n):
            ans = []

            while n:
                ans.append(n % 2)
                n //= 2

            return ans + [0] * (32 - len(ans))
        
        def bit2int(arr):
            ans = 0
            curr_bit_val = 1

            for bit in reversed(arr):
                ans += curr_bit_val * bit
                curr_bit_val *= 2
            
            return ans

        return bit2int(int2reversed_bit(n))