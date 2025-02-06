class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        count = dict()

        # Initialize counter for every possible product value
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j] 

                if prod not in count:
                    count[prod] = 0
                count[prod] += 1

        num_tuples = 0 

        # Count number of tuple (a, b, c, d) - order does not matter!
        for i in range(n):
            for j in range(i + 1, n):
                num_tuples += count[nums[i] * nums[j]] - 1

        return num_tuples * 4
