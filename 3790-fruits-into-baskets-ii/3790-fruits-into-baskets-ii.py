class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt = 0
        available = [True for _ in range(len(baskets))]

        for fruit in fruits:
            for idx, basket in enumerate(baskets):
                if fruit <= basket and available[idx]:
                    cnt += 1
                    available[idx] = False
                    break
        
        return len(fruits) - cnt