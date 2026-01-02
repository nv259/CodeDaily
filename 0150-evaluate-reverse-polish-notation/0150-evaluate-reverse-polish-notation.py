class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    c = a + b
                elif token == '-':
                    c = a - b
                elif token == '*':
                    c = a * b
                elif token == '/':
                    c = int(a / b)
                
                stack.append(c)
            else:
                stack.append(int(token))
        
        return stack[-1]

# Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
             
        