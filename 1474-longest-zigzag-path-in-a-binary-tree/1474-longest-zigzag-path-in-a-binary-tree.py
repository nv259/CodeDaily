# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, previous_branch, path_length=-1):
            if not node: return path_length

            if previous_branch == 'left':
                return max(
                    dfs(node.left, 'left', 0),
                    dfs(node.right, 'right', path_length + 1)
                )
            else:
                return max(
                    dfs(node.left, 'left', path_length + 1),
                    dfs(node.right, 'right', 0)
                )

        return dfs(root, 'left')