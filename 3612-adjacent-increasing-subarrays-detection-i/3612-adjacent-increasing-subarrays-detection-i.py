class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        il, ir = 0, 0
        jl, jr = k, k

        def check(l, r, size_):
            return r - l + 1 == size_

        while jr < n and ir < n - k:
            # if i's window has k elements => OK
            # if j's window has k elements => OK
            if check(il, ir, k) and check(jl, jr, k):
                return True

            # slide i's window (left)
            ir += 1
            if ir < n - k and nums[ir] <= nums[ir - 1]: 
                il = ir
                jl = il + k
                jr = jl
                continue

            # slide j's window (right)
            jr += 1
            if jr >= n: return False
            if jr < n and nums[jr] <= nums[jr - 1]:
                jl = jr
                il = jl - k 
                ir = il

        # Recheck
        if check(il, ir, k) and check(jl, jr, k):
            return True

        return False