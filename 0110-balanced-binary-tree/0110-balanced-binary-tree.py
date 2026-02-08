# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def visit(node, is_balanced=True):
            if not node: return [0, True]

            node.left_cnt, is_balanced = visit(node.left)
            if not is_balanced: return [0, False]
            node.right_cnt, is_balanced = visit(node.right)
            if not is_balanced: return [0, False]

            return [max(node.left_cnt, node.right_cnt) + 1, abs(node.left_cnt - node.right_cnt) <= 1]
    
        return visit(root)[1]
            

            
            