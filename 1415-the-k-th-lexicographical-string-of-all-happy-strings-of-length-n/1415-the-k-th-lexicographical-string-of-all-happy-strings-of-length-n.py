class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.ans = ""
        self.counter = 0
        happy_string = [''] * n

        def generate(i):
            if self.counter == k:
                return

            if i == n:
                self.counter += 1
                if self.counter == k:
                    self.ans = "".join(happy_string)
                return
            
            for c in "abc":
                if i == 0 or c != happy_string[i - 1]:
                    happy_string[i] = c
                    generate(i + 1)
                
            return

        if k <= 3 * 2**(n - 1):
            generate(0)
        return self.ans