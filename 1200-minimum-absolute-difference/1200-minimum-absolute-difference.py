class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dist = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))

        ans = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_dist:
                ans.append([arr[i], arr[i + 1]])
            
        return ans