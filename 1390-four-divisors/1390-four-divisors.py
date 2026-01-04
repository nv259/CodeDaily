class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if num == 1: continue

            # Count divisor
            divisor_sum = num + 1
            divisor_cnt = 2
            for i in range(2, int(num**0.5) + 1):
                if divisor_cnt > 4: break
                if num % i == 0: 
                    divisor_cnt += 1
                    if num // i != i: divisor_cnt += 1

                    divisor_sum += i + (num // i)

            if divisor_cnt != 4: continue
            ans += divisor_sum

        return ans
