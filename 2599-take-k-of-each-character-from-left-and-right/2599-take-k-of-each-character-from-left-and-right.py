class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        # Constraint: each character appears at least `k` times.
        # And we want to find the shortest valid one
        # We can find the valid windows and choose the shortest
        # However, we can also choose both left-most and right-most character.
        # To this end, we can double the given string and use a simple sliding window
        n = len(s)
        s = s + s
        l, r = 0, 0
        freq = { 'a': 0, 'b': 0, 'c': 0 }
        res = float("inf")

        # Slide window to the right
        # i.e., increase the size of window until it valid
        while r < len(s):
            # print(s[l:r + 1], res)
            freq[s[r]] += 1
            
            if freq['a'] >= k and freq['b'] >= k and freq['c'] >= k:
                if r - l + 1 <= n: 
                    res = min(res, r - l + 1)

            # Shorten the window if it is a valid one
            while freq['a'] >= k and freq['b'] >= k and freq['c'] >= k and l < n and r >= n - 1:
                # print('\t', s[l: r + 1], res)
                if r - l + 1 <= n: 
                    res = min(res, r - l + 1)
                freq[s[l]] -= 1
                l += 1

            r += 1

        return -1 if res == float("inf") else res
