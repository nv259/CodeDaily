class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n_bit = list(bin(n))
        for i in range(2, len(n_bit)):
            n_bit[i] = '0' if n_bit[i] == '1' else '1'
        return int("".join(n_bit[2:]), 2)