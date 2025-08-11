class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        final_id, id1, id2 = m + n - 1, m - 1, n - 1
        while final_id >= 0:
            if id1 < 0 or id2 < 0: break

            if nums1[id1] >= nums2[id2]:
                nums1[final_id] = nums1[id1]
                id1 -= 1
            else:
                nums1[final_id] = nums2[id2]
                id2 -= 1
            final_id -= 1
        
        while id2 >= 0:
            nums1[final_id] = nums2[id2]
            final_id -= 1
            id2 -= 1