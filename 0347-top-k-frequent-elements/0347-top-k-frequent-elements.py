from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnt = Counter(nums)
        cnt_num = {}
        for num, cnt in num_cnt.items():
            if cnt not in cnt_num:
                cnt_num[cnt] = []
            cnt_num[cnt].append(num)

        ans = []
        for cnt in sorted(cnt_num.keys(), reverse=True):
            if k == 0: break
            ans += cnt_num[cnt] 
            k -= len(cnt_num[cnt]) 
            
        return ans
            
        