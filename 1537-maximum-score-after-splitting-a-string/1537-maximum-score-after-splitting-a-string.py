class Solution:
    def maxScore(self, s: str) -> int:
        def prefix_count(arr, value):
            """ Return the prefix count of the appearance of value,
                f[i]: the number of times value appears in range [0, i]
            """
            value = str(value)

            f = [0 for _ in range(len(arr))] 

            for idx, val in enumerate(arr):
                if idx != 0:
                    f[idx] = f[idx - 1] 
                
                f[idx] = f[idx] + 1 if val == value else f[idx]

            return f
        
        prefix_zeros_count = prefix_count(s, 0)
        suffix_ones_count = prefix_count(s[::-1], 1)[::-1]

        ans = 0
        for i in range(len(s) - 1):
            # print(prefix_zeros_count[i], suffix_ones_count[i + 1])
            ans = max(ans, prefix_zeros_count[i] + suffix_ones_count[i+1])
        
        return ans