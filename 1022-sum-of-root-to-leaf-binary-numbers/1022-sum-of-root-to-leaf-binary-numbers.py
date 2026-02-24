# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], curr_val=0) -> int:
        curr_val = (curr_val << 1) + root.val
        if root.left is None and root.right is None: return curr_val

        if root.left is not None:
            sum_left = self.sumRootToLeaf(root.left, curr_val)
        else:
            sum_left = 0
        if root.right is not None:
            sum_right = self.sumRootToLeaf(root.right, curr_val)
        else:
            sum_right = 0
        
        return sum_left + sum_right
        





        

