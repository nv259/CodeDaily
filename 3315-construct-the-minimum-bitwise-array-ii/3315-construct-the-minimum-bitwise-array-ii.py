class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num == 2: 
                ans.append(-1)
                continue

            bin_num = bin(num)
            i = len(bin_num) - 1
            while i >= 0:
                if bin_num[i] != '1': 
                    break
                i -= 1
            bin_num = bin_num[:i + 1] + '0' + bin_num[i + 2:]

            ans.append(int(bin_num, 2))
        
        return ans
 