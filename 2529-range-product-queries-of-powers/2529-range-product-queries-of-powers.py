class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        modulo = int(1e9) + 7

        def find_powers(n):
            ans = []
            curr = 1

            while n:
                if n % 2 == 1:
                    ans.append(curr)
                curr *= 2         
                n //= 2
            
            return ans


        # Find powers
        powers = find_powers(n)

        # Calculate cumulative product for powers
        curr_prod = 1
        cum_prod = []
        for power in powers:
            curr_prod *= power
            # curr_prod %= modulo
            cum_prod.append(curr_prod)

        # Process each query in queries
        res = []
        for left, right in queries:
            if left == 0:
                res.append(cum_prod[right] % modulo)
            else:
                res.append((cum_prod[right] // cum_prod[left - 1]) % modulo)
        
        return res
