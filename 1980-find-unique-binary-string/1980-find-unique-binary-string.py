class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def to_bits(n):
            if n == 0: return '0' * len(nums)

            ans = ""
            while n:
                ans += str(n % 2)
                n //= 2
            
            return '0' * (len(nums) - len(ans)) + ans[::-1]
        
        def to_int(bits):
            ans = 0
            for bit in bits:
                ans = (ans << 1) + int(bit)
             
            return ans

        nums = set([to_int(ele) for ele in nums])
        for num in range(0, 2**len(nums)):
            if num not in nums:
                return to_bits(num)
        
        return -1