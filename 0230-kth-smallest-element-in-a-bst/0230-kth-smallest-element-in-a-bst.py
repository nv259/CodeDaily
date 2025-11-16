# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []
        
        def traverse_depth_first(node):
            if node.left:
                traverse_depth_first(node.left)
            arr.append(node.val)
            if node.right:
                traverse_depth_first(node.right)

        traverse_depth_first(root)

        return arr[k - 1]
        