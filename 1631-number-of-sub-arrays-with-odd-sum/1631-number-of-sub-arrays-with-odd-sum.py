class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        cum_sum = 0
        odd_cnt, even_cnt = 0, 0

        for num in arr:
            cum_sum += num

            res += odd_cnt if cum_sum % 2 == 0 else even_cnt
            if cum_sum % 2 != 0:
                res += 1
                odd_cnt += 1
            else: 
                even_cnt += 1
        
        return res % (int(1e9) + 7)