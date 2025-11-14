from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_counter = Counter(s)
        is_used = {}
        for char in char_counter.keys():
            is_used[char] = False

        # monotonic increasing stack
        stack = []  # [char]

        for c in s:
            # pop until valid
            while len(stack) and (not is_used[c]) and (c < stack[-1] and char_counter[stack[-1]] >= 1):
                char = stack.pop()
                is_used[char] = False

            # push the current char onto top of the stack
            if not is_used[c]:
                stack.append(c)
                is_used[c] = True
            char_counter[c] -= 1

        ans = ""
        for char in stack:
            if char not in ans:
                ans += char

        return ans