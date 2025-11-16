# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def assign_no_lr_children(node):
    if node is None: return 0

    node.left_cnt = 0
    node.right_cnt = 0

    if node.left:
        node.left_cnt = assign_no_lr_children(node.left)
    if node.right:
        node.right_cnt = assign_no_lr_children(node.right)
    
    return node.left_cnt + node.right_cnt + 1


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        assign_no_lr_children(root)

        def find_kth_smallest(node, k):
            # Miss
            if node is None: return None

            # Hit
            if k == node.left_cnt + 1:
                return node.val 
            
            # Branching
            if k <= node.left_cnt:
                return find_kth_smallest(node.left, k)
            else:
                return find_kth_smallest(node.right, k - node.left_cnt - 1)
        
        return find_kth_smallest(root, k)

        