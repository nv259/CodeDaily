class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k >= len(s): return False
        s = [int(c) for c in s]

        curr = 0
        msb_value = 1
        nums_bin_code = 0
        for i in range(k - 1, -1, -1):
            curr += s[i] * msb_value
            nums_bin_code += msb_value
            msb_value *= 2
        msb_value //= 2
        
        codes = [curr]
        for i in range(k, len(s)):
            curr -= s[i - k] * msb_value
            curr = (curr << 1) + s[i]

            codes.append(curr)
        
        return len(set(codes)) == nums_bin_code + 1

         