class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        base = 1_000
        commas_used = 1

        while base * 1_000 <= n:
            num_cnt = base * 1_000 - base
            ans += commas_used * num_cnt
            base *= 1_000
            commas_used += 1

        if n >= base:
            ans += (n - base + 1) * commas_used

        return ans