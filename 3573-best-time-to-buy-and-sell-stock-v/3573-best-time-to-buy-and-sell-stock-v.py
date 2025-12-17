class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)
        # 0: sell
        # 1: buy
        dp = [[[float('-inf'), float('-inf')] for j in range(2 * k)]
              for i in range(N)]    # N x k x 2
        ans = 0

        for i in range(N):
            for j in range(min(i + 1, 2 * k)):
                if j == 0:
                    dp[i][j][0] = max(dp[i - 1][j][0], prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], -prices[i])
                # begin a transaction
                elif j % 2 == 0:
                    prev_max = max(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1])
                    # short-selling
                    dp[i][j][0] = max(
                        dp[i - 1][j][0],    # do nothing
                        prev_max + prices[i]   # sell out stock at i-th day
                    )

                    # normal transaction
                    dp[i][j][1] = max(
                        dp[i - 1][j][1],    # do nothing
                        prev_max - prices[i]   # buy in stock at i-th day
                    )
                elif j % 2 == 1:   # complete a transaction
                    # normal transaction
                    dp[i][j][0] = max(
                        dp[i - 1][j][0],    # do nothing
                        dp[i - 1][j - 1][1] + prices[i] # sell stock
                    )

                    # short-selling
                    dp[i][j][1] = max(
                        dp[i - 1][j][1],    # do nothing
                        dp[i - 1][j - 1][0] - prices[i] # buy stock
                    )
                    ans = max(ans, dp[i][j][0], dp[i][j][1])
            #     print(dp[i][j][0], dp[i][j][1], end=' | ')
            # print()

        return ans