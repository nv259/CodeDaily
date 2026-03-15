class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        N = len(nums)

        if N <= 2: return N
        
        def longest_arithmetic_ends(nums):
            ans = [1] * N
            ans[1] = 2

            for i in range(2, N):
                if (nums[i] - nums[i - 1]) == (nums[i - 1] - nums[i - 2]):
                    ans[i] = ans[i - 1] + 1
                else:
                    ans[i] = 2

            return ans

        left_longest_arithmetic_ends_at = longest_arithmetic_ends(nums)
        right_longest_arithmetic_ends_at = longest_arithmetic_ends(nums[::-1])[::-1]
        # print(left_longest_arithmetic_ends_at)
        # print(right_longest_arithmetic_ends_at)

        ans = max(left_longest_arithmetic_ends_at
                 + right_longest_arithmetic_ends_at)

        for i in range(N):
            # print(i, end='\t')
            # if i == 0:
            if i + 2 < N:
                # replace
                modified_num = nums[i + 1] + (nums[i + 1] - nums[i + 2])
                ans = max(ans, right_longest_arithmetic_ends_at[i + 1] + 1)
                # print(modified_num, ans)
            if i - 2 >= 0:
            # elif i == N - 1:
                # replace
                modified_num = nums[i - 1] + (nums[i - 1] - nums[i - 2])
                ans = max(ans, left_longest_arithmetic_ends_at[i - 1] + 1)
                # print(modified_num, ans)
            
            if (i + 1 < N and i - 1 >= 0) and (nums[i - 1] + nums[i + 1]) % 2 == 0:
                # replace
                modified_num = (nums[i - 1] + nums[i + 1]) // 2
                # print(modified_num)

                longest_subarr = 1
                if i - 2 >= 0 and (modified_num - nums[i - 1]) == (nums[i - 1] - nums[i - 2]):
                    longest_subarr += left_longest_arithmetic_ends_at[i - 1]
                else:
                    longest_subarr += 1

                if i + 2 < N and (nums[i + 1] - modified_num) == (nums[i + 2] - nums[i + 1]):
                    longest_subarr += right_longest_arithmetic_ends_at[i + 1]
                else:
                    longest_subarr += 1

                ans = max(ans, longest_subarr)
                # print(modified_num, longest_subarr)
            # else:
            #     ans = max(ans, right_longest_arithmetic_ends_at[i + 1] + 1)
            #     ans = max(ans, left_longest_arithmetic_ends_at[i - 1] + 1)
            #     print()
            
        return ans
