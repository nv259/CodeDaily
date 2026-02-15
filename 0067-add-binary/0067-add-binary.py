class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b): 
            a, b = b, a

        a = [int(c) for c in a]
        b = [0] * (len(a) - len(b)) + [int(c) for c in b]
        c = [0] * len(a)
        remain = 0
        bit_idx = -1

        while abs(bit_idx) <= len(b):
            _sum = a[bit_idx] + b[bit_idx] + remain
            c[bit_idx] = _sum % 2
            remain = _sum // 2
            bit_idx -= 1
        
        c = "".join([str(element) for element in c])

        if remain == 1:
            c = '1' + c
        
        return c
        