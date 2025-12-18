class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        N = len(prices)
        def calc_prefix_sum(prices, strategy):
            prefix_sum = [0] * N
            for idx, (price, action) in enumerate(zip(prices, strategy)):
                prefix_sum[idx] = prefix_sum[idx - 1] + price * action
            
            return prefix_sum
    
        def calc_consecutive_sum(prefix_sum, l, r):
            return prefix_sum[r] - prefix_sum[l - 1]

        strategy_prefix_sum = calc_prefix_sum(prices, strategy)
        strategy_prefix_sum.append(0)
        # print(strategy_prefix_sum)
        strategy_suffix_sum = calc_prefix_sum(prices[::-1], strategy[::-1])[::-1]
        strategy_suffix_sum.append(0)
        # print(strategy_suffix_sum)
        all_sell_prefix_sum = calc_prefix_sum(prices, [1] * N)
        all_sell_prefix_sum.append(0)
        # print(all_sell_prefix_sum)
        ans = strategy_prefix_sum[N - 1]

        for i in range(k - 1, N):
            # modify [i - k + 1, i]
            ans = max(ans, strategy_prefix_sum[i - k] + strategy_suffix_sum[i + 1]
                            + calc_consecutive_sum(all_sell_prefix_sum, i - (k // 2) + 1, i))
        
        return ans 