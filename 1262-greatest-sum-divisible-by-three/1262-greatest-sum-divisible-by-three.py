class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        N = len(nums)

        # dp[i][mod]: the maximum possible sum upto `i` 
        # (whether chosen or not)
        # and has the remain after divided by 3 is `mod`
        dp = [[0 for mod in range(3)]
              for i in range(N)]
        dp[0][nums[0] % 3] = nums[0]

        ans = 0
        for i in range(1, N):
            for mod in range(3):
                # Do not take in nums[i] as default
                prev_mod = (mod - nums[i] % 3) % 3

                if (dp[i - 1][prev_mod] + nums[i]) % 3 != mod:
                    dp[i][mod] = dp[i - 1][mod]
                else:
                    dp[i][mod] = max(dp[i - 1][mod], dp[i - 1][prev_mod] + nums[i])
        
        return dp[-1][0]