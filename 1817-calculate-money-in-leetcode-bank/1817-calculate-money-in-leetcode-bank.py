class Solution:
    def totalMoney(self, n: int) -> int:
        weeks_count = n // 7
        remain_days = n % 7

        ans = 21 * weeks_count + 7 * weeks_count * (weeks_count + 1) / 2

        # monday
        money_put = weeks_count + 1
        for idx in range(remain_days):
            ans += money_put
            money_put += 1

        return int(ans)