class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Find NEG for every element in nums2
        neg = {}
        stack = []
        i, N = 0, len(nums2)
        
        while i < N:
            while len(stack) != 0 and nums2[i] > stack[-1]:
                j = stack.pop()
                neg[j] = nums2[i]

            stack.append(nums2[i])
            i += 1

        while len(stack):
            j = stack.pop()
            neg[j] = -1

        return [neg[num] for num in nums1]
        