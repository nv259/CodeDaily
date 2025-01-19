class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = []

        for i, price in enumerate(prices):
            for j in range(i + 1, n):
                if price >= prices[j]:
                    price -= prices[j]
                    break
            res.append(price)         
            
        return res