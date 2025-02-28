class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        existed_values = set(arr)

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                prev = arr[j]
                curr = arr[i] + arr[j] 
                curr_len = 2

                while curr in existed_values:
                    prev, curr = curr, curr + prev
                    curr_len += 1
                    res = max(res, curr_len)

        return res