class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = deque()
        p_len = len(part)

        for c in s:
            stack.append(c)

            if len(stack) >= p_len:
                tmp = "".join(stack.pop() for _ in range(p_len))[::-1]
                
                if tmp != part:
                    for cc in tmp: stack.append(cc)
        
        return "".join(stack)