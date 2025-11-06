# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class AVLTree:
    def __init__(self, root=None):
        self.root = root

    def rebalance(self, root):
        balance_factor = self.balance_factor(root)

        # LL imbalance
        if balance_factor < -1 and self.balance_factor(root.left) < 0:
            return self._right_rotate(root)
        
        # RR imbalance
        if balance_factor > 1 and self.balance_factor(root.right) > 0:
            return self._left_rotate(root)
        
        # LR imbalance
        if balance_factor < -1 and self.balance_factor(root.left) > 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        
        # RL imbalance
        if balance_factor > 1 and self.balance_factor(root.right) < 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        
        return root

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.right) - self.height(node.left)

    def height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _insert(self, root, val):
        if root is None:
            node = TreeNode(val)
            node.height = 1 
            return node
        
        if val > root.val:
            root.right = self._insert(root.right, val)
        elif val < root.val:
            root.left = self._insert(root.left, val)
        
        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        return self.rebalance(root)

    def _left_rotate(self, x):        
        y = x.right
        tmp = y.left

        y.left = x
        x.right = tmp
        
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    def _right_rotate(self, x):
        y = x.left
        tmp = y.right
        
        y.right = x
        x.left = tmp

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def _delete(self, root, val):
        pass
    
    def _search(self, root, val):
        pass
        
    def insert(self, val):
        self.root = self._insert(self.root, val)

# from typing import Optional

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # def balanceBST(self) -> Optional[TreeNode]:
        # order traversal through entire tree to get the increasing array      
        nums = []
        def inorder_traversal(root):
            if root is None:
                return
                
            if root.left:
                inorder_traversal(root.left)
            nums.append(root.val)
            if root.right:
                inorder_traversal(root.right)
     
        inorder_traversal(root)
        print(nums) 
        # nums = [2500, 5000, 7500, 10000, 12500, 15000, 17500]
            
        tree = AVLTree()
        for num in nums:
            tree.insert(num)
        
        return tree.root