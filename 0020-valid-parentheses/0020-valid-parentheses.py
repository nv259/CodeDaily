class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                # No open bracket in stack
                if len(stack) == 0:
                    return False

                # Close bracket must follow an open bracket
                if c == ')' and stack[-1] != '(':
                    return False
                if c == ']' and stack[-1] != '[':
                    return False
                if c == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        
        return True if len(stack) == 0 else False
    