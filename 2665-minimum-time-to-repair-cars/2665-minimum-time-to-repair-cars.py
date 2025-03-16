class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(time):
            total_car = 0

            for rank in ranks:
                total_car += int((time // rank) ** 0.5)
        
            return total_car >= cars


        low, high = 0, min(ranks) * cars * cars + 1
        ans = None

        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans