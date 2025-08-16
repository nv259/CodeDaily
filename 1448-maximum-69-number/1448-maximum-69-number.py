class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for idx, char in enumerate(num):
            if char == '6':
                num[idx] = '9'
                return int(''.join(num))

        return int(''.join(num)) 