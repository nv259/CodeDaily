class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def _recurr(amount, cnt):
            if amount == 0:
                return cnt

            if amount in memo:
                return memo[amount] + cnt

            min_cnt = float("inf")
            for coin in coins:
                if amount - coin < 0: continue
                # print(f"amount {amount}, coin {coin}, cnt {cnt}")
                min_cnt = min(min_cnt, _recurr(amount - coin, 1))

            if amount not in memo:
                memo[amount] = min_cnt

            # print(f"memo[{amount}] = {memo[amount]}")

            return min_cnt + cnt

        ans = _recurr(amount, 0)
        if ans == float("inf"):
            return -1
        
        return ans
