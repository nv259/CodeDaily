class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        def calc_prefix_sum(arr, key):
            ans = [0] * N
            for i, ele in enumerate(arr):
                tmp = 1 if ele == key else 0
                ans[i] = ans[i - 1] + tmp
            
            return ans 

        prefix_sum = [0] + calc_prefix_sum(customers, key='N')
        suffix_sum = calc_prefix_sum(customers[::-1], key='Y')[::-1]
        suffix_sum.append(0)

        min_penalty = float('inf')
        optimal_hour = N
        for i in range(N, -1, -1):
            penalty = prefix_sum[i] + suffix_sum[i]
            if min_penalty >= penalty:
                min_penalty = penalty
                optimal_hour = i
    
        return optimal_hour