class Solution:
    def smallestNumber(self, pattern: str) -> str:
        is_used = [False for _ in range(10)]
        
        def is_valid(num):
            for i, part in enumerate(pattern):
                if ((part == 'I' and num[i] < num[i + 1]) or
                    (part == 'D' and num[i] > num[i + 1])):
                    continue
                else: 
                    return False
            return True
        
        def recur(num):
            if len(num) == len(pattern) + 1:
                if is_valid(num):
                    return num
            
            for digit in range(1, 10):
                if not is_used[digit]:
                    is_used[digit] = True

                    ans = recur(num + str(digit))
                    if ans is not None: return ans

                    is_used[digit] = False

            return None

        return recur('')