# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums from List to Set for O(1) access time
        nums = set(nums)

        def remove_nums(node, nums):
            if node is None: return None

            if node.val in nums:
                return remove_nums(node.next, nums)
            else:
                node.next = remove_nums(node.next, nums)
                return node

        return remove_nums(head, nums) 