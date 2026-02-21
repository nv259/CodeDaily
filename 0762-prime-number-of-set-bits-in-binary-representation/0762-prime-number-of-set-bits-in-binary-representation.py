class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def gather_prime(lo=2, hi=20):
            ans = []
            for i in range(lo, hi):
                is_prime = True
                for j in range(2, int(sqrt(i)) + 1):
                    if i % j == 0:
                        is_prime = False
                        break
                
                if is_prime: ans.append(i)

            return ans
        
        def count_set_bit(n):
            # init with lsb
            ans = 0

            while n:
                ans += n % 2
                n //= 2
            
            return ans

        primes = [2, 3, 5, 7, 11, 13, 17, 19]

        return sum(count_set_bit(i) in primes for i in range(left, right + 1))
        