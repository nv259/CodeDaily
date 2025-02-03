class Solution:
    def removeStars(self, s: str) -> str:
        res = deque()

        for char in s:
            if char != '*': 
                res.append(char)
            elif char == '*' and res:
                res.pop()

        return ''.join(res)