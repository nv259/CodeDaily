class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def cnt_set_bit(n):
            ans = 0
            while n:
                ans += n % 2
                n //= 2
            return ans
        
        arr = sorted([[cnt_set_bit(ele), ele] for ele in arr])
        return [ele for _, ele in arr]
