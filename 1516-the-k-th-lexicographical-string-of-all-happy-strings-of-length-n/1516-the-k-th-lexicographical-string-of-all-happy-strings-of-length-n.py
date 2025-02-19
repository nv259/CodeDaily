class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strs = []

        def backtrack(string):
            if len(happy_strs) >= k:
                return happy_strs[k - 1]

            if len(string) == n + 1:
                happy_strs.append(string)
                return ""

            for char in ('a', 'b', 'c'):
                if char != string[-1]:
                    ans = backtrack(string + char)

                    if ans != "":
                        return ans
            
            return ""

        backtrack("x")

        return happy_strs[-1][1:] if len(happy_strs) >= k else ""