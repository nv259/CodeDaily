class Solution:
    def minimumDeletions(self, s: str) -> int:
        # s = [ord(c) - ord('a') for c in s]
        N = len(s)
        ans = 0
        f = ['c'] * N

        def bin_search(arr, key):
            ans = -1
            low, high = 0, len(arr)
            
            while low <= high:
                mid = (low + high) // 2

                if arr[mid] > key:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            return ans

        for i in range(N):
            idx = bin_search(f, s[i])
            ans = max(ans, idx + 1)
            # print(f, idx, ans)
            f[idx] = s[i]

        return N - ans
