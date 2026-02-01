class Solution:
    def countMonobit(self, n: int) -> int:
        curr_val = 1
        curr_bit = 1
        ans = 0
        
        while curr_val <= n:
            ans += 1
            curr_bit *= 2
            curr_val = curr_val + curr_bit

        return ans + 1