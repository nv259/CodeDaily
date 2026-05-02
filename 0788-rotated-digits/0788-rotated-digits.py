class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotated_digits = {
            '0': '0', '1': '1', '2': '5', 
            '5': '2', '6': '9', '8': '8', '9': '6'
        }

        def is_good_number(num):
            if not all(c in rotated_digits for c in str(num)):
                return False

            rotated_num = int(''.join([rotated_digits[c] for c in str(num)]))
            return rotated_num != num

        good_cnt = 0
        for num in range(1, n + 1):
            good_cnt += is_good_number(num)
        
        return good_cnt