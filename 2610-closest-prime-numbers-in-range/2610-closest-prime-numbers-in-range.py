class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True for _ in range(right + 1)]
        is_prime[1] = False

        prime_nums = []
        diff = float("inf")

        for i in range(2, right + 1):
            if is_prime[i]:
                for j in range(i*2, right + 1, i):
                    is_prime[j] = False

                if i >= left:
                    prime_nums.append(i)
    
                    if len(prime_nums) >= 2:
                        if diff > prime_nums[-1] - prime_nums[-2]:
                            num1 = prime_nums[-2]
                            num2 = prime_nums[-1]
                            diff = num2 - num1
            
        if len(prime_nums) < 2:
            return [-1, -1]
        else:
            return [num1, num2]