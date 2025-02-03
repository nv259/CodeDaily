class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        def missing_nums(x, y):
            """ return all numbers in x that not exists in y """
            y_nums = { num: True for num in y }
            characterized_x_nums = []

            for num in x:
                if num not in y_nums:
                    characterized_x_nums.append(num)

            return list(set(characterized_x_nums))

        return [missing_nums(nums1, nums2), missing_nums(nums2, nums1)]