class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # maximum value in range [0, end]
        accum_max = {0: 0}
        end_moments = [0]
        events = [[end, start, val] for start, end, val in events]
        events.sort()
        ans = 0
        
        def binary_search(arr, key):
            ans = -1
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2

                if arr[mid] <= key:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1

            return ans

        for end, start, curr_value in events:
            idx = binary_search(end_moments, start - 1)
            if idx == -1: print("hehe")   # no chance this happens
            # idx = bisect.bisect_left(end_moments, start - 1) - 1
            prev_max_value = accum_max[end_moments[idx]]
            ans = max(ans, prev_max_value + curr_value)
            
            if end not in accum_max:
                accum_max[end] = 0
            idx = binary_search(end_moments, end)
            prev_max_value = accum_max[end_moments[idx]]
            accum_max[end] = max(accum_max[end], prev_max_value, curr_value)
            end_moments.append(end)

        return ans