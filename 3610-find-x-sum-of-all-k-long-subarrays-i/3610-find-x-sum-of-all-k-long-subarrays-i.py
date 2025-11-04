class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def record(cnt, num):
            if num not in cnt:
                cnt[num] = 0
            cnt[num] += 1

        n = len(nums)
        cnt = {}    # num: no_num

        # initial pass
        for j, num in enumerate(nums[:k]):
            record(cnt, num)

        def x_sum(cnt):
            pq = []
            for num, num_cnt in cnt.items():
                heapq.heappush(pq, (-num_cnt, -num))
    
            ans = 0
            for _ in range(x):
                if not pq:
                    break
                num_cnt, num = heapq.heappop(pq)
                ans += num * num_cnt

            return ans
    
        ans = [x_sum(cnt)]

        j += 1
        while j < n:
            record(cnt, nums[j])
            # increase cnt[nums[j]]
            num = nums[j]

            # decrease cnt[nums[j - k]]
            cnt[nums[j - k]] -= 1
            if cnt[nums[j - k]] == 0:
                del cnt[nums[j - k]]
            
            ans.append(x_sum(cnt))
            j += 1

        return ans 