rotated_digits = {
    '0': '0', '1': '1', '2': '5', 
    '5': '2', '6': '9', '8': '8', '9': '6'
}
good_cnt = [0] * (10**4 + 1)

def is_good_number(num):
    if not all(c in rotated_digits for c in str(num)):
        return False

    rotated_num = int(''.join([rotated_digits[c] for c in str(num)]))
    return rotated_num != num

for num in range(1, 10**4 + 1):
    good_cnt[num] = good_cnt[num - 1] + is_good_number(num)


class Solution:
    def rotatedDigits(self, n: int) -> int:
        return good_cnt[n]