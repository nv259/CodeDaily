class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0: return -1

        n = 1
        cnt = 1
        while cnt <= int(1e6):
            # print(cnt, n)
            if n % k == 0: return cnt

            n = (n * 10 + 1) % k
            cnt += 1

        return -1
