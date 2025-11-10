class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = deque()
        ans = 0

        for num in nums:
            while stack and num < stack[0]:
                stack.popleft()

            if num == 0: continue

            if len(stack) == 0 or num != stack[0]:
                ans += 1
                stack.appendleft(num)

        return ans