class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations) 

        def check(stations, minimum_power):
            stations_ = [station for station in stations]

            # inital first window
            power_i = sum(stations_[: 2*r + 1])
            remains = k

            # slide the window to the right
            for i in range(r + 1, r + n + 1):
                # add new, subtract old
                power_i -= stations_[i - r - 1]
                power_i += stations_[i + r]

                if power_i < minimum_power:
                    delta = minimum_power - power_i
                    
                    # if not enough building to satisfy the requirement
                    if delta > remains:
                        return False

                    power_i += delta
                    stations_[i + r] += delta
                    remains -= delta
            
            return True
        
        low, high = 0, sum(stations) + k
        stations = [0] * (r + 1) + stations + [0] * (r + 1)
        ans = 0
        while low <= high:
            mid = (low + high) // 2

            if check(stations, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans