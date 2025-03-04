class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        prev_exponent = 15
        while n:
            check = False

            for exponent in reversed(range(prev_exponent)):
                value = 3 ** exponent
                if n >= value:
                    n -= value
                    prev_exponent = exponent
                    check = True
                    break
            
            if not check:
                return False
        
        return True
                