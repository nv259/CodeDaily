class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic decreasing stack
        stack = []

        for i, price in enumerate(prices):
            while len(stack) and price <= prices[stack[-1]]:
                j = stack.pop()
                prices[j] -= price

            stack.append(i)
             
        return prices 
        