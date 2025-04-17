class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pos_dict = {}   # val: [pos]

        for idx, num in enumerate(nums):
            if num not in pos_dict:
                pos_dict[num] = [idx]
            else:
                heapq.heappush(pos_dict[num], idx)
        ans = 0
        for val, pos_list in pos_dict.items():
            undivisable_cnt = 0
            for idx, pos in enumerate(pos_list):
                for pos_j in pos_list[idx + 1:]:
                    if (pos * pos_j) % k == 0:
                        ans += 1
        
        return ans