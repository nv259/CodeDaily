class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def calculate_digits_sum(num):
            ans = 0

            while num:
                ans += num % 10
                num = num // 10
            
            return ans

        dic = dict()    # sum of digits : [num with sum of digits] 

        for num in nums:
            digits_sum = calculate_digits_sum(num)
            
            if digits_sum not in dic:
                dic[digits_sum] = []
            dic[digits_sum].append(num)

        res = -1
        for digits_sum in dic.keys():
            if len(dic[digits_sum]) >= 2:
                dic[digits_sum].sort()
                res = max(res, dic[digits_sum][-1] + dic[digits_sum][-2])
        
        print(dic)

        return res          
