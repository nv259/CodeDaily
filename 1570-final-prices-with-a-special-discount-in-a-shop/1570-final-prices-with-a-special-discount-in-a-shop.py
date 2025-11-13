class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic 
        stack = []      

        for i in range(len(prices) - 1, -1, -1):
            while len(stack) and prices[i] < stack[-1]:
                stack.pop()

            original_price = prices[i]
            if len(stack):
                prices[i] -= stack[-1]
            stack.append(original_price)

        return prices