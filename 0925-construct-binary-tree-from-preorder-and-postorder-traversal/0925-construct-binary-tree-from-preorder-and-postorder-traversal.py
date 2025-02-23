# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        print(preorder, '-', postorder)
        if len(preorder) == 0: return None

        root = TreeNode(preorder[0])
        
        if len(preorder) == 1: 
            return root # does not have any child

        # assume that root always has left child
        ## define the left_subtree
        for idx in range(len(postorder) - 1, -1, -1):
            if postorder[idx] == preorder[1]: break

        root.left = self.constructFromPrePost(preorder[1: idx + 2], postorder[: idx + 1])

        # if it still remains some elements, assign it to the right subtree
        root.right = self.constructFromPrePost(preorder[idx + 2: ], postorder[idx + 1: -1])

        return root