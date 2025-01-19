class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l, r = 0, 0
        s = s + ' '
        prev_token = -1

        while r < len(s):
            if s[l].isdigit():
                if s[r].isdigit():
                    r += 1
                else:
                    if int(s[l:r]) <= prev_token:
                        return False
                    else:
                        prev_token = int(s[l:r])
                        l = r
            else:
                l += 1
                r = l

        return True     