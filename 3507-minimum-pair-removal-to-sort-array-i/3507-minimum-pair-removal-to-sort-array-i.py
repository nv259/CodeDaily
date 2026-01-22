class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr): 
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            
            return True

        ans = 0
        while not is_non_decreasing(nums):
            N = len(nums)
            # Utilize monotonic stack to find idx with minimum adj pair sum
            stack, i = [], 0
            while i < N - 1:
                while len(stack) and (nums[stack[-1]] + nums[stack[-1] + 1] > nums[i] + nums[i + 1]):
                    stack.pop()
                stack.append(i)
                print(stack)

                i += 1  
            
            i = stack[0]
            left = nums[: i]
            right = [] if i + 2 >= N else nums[i + 2:]
            nums = left + [nums[i] + nums[i + 1]] + right
            ans += 1

        return ans