class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        sunny_days = []
        for day in range(len(rains)):
            if rains[day] == 0:
                sunny_days.append(day)
        
        # print(sunny_days)
        
        ans = [0] * len(rains)

        def binary_search(arr, check, u, v):
            low, high = 0, len(arr) - 1
            ans = -1 

            while low <= high:
                mid = (low + high) // 2
                # print('\t', mid, arr[mid])

                if arr[mid] < u:
                    low = mid + 1
                elif arr[mid] > v:
                    high = mid - 1
                elif u <= arr[mid] <= v:
                    # if check[arr[mid]]:
                    #     low = mid + 1
                    # else:
                    ans = arr[mid]
                    high = mid - 1
                
                # print('\t\t', ans)
                
            # arr.discard(ans)
            if ans != -1:
                arr.remove(ans)
            return ans
                    

        full_lake = {}
        for day, rainy_lake in enumerate(rains):
            if rainy_lake != 0:
                if rainy_lake not in full_lake:
                    full_lake[rainy_lake] = day
                else:
                    cleaning_day = binary_search(sunny_days, ans, full_lake[rainy_lake] + 1, day - 1)
                    # print(rainy_lake, full_lake[rainy_lake], day, cleaning_day)
                    if cleaning_day == -1:
                        return []

                    ans[cleaning_day] = rainy_lake
                    full_lake[rainy_lake] = day

                ans[day] = -1
            else:
                # do nothing
                pass
            
            # print(ans)

        for day in range(len(ans)):
            if ans[day] == 0:
                ans[day] = 1

        return ans