# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []
        def inorder_traversal(node):
            if node is None: return
            
            if node.left:
                inorder_traversal(node.left)
            nums.append(node.val)
            if node.right:
                inorder_traversal(node.right)
        
        inorder_traversal(root)
        print(nums)

        def build_balanced_tree(left, right):
            if left > right: return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = build_balanced_tree(left, mid - 1)
            node.right = build_balanced_tree(mid + 1, right)

            return node
        
        return build_balanced_tree(0, len(nums) - 1)
