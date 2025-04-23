def sum_digits(x):
    ret = 0
    while x:
        ret += x % 10
        x //= 10
    return ret

class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = [0] * (9*5)
        max_size = 0
        for i in range(1, n + 1):
            tmp = sum_digits(i)
            counter[tmp] += 1
            max_size = max(max_size, counter[tmp])
        
        return sum([max_size == cnt for cnt in counter])