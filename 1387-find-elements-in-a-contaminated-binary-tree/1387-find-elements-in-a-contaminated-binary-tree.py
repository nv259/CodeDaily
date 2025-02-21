# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode], val=0):
        self.root = root
        self.values = []

        def recover(node, val):
            self.values.append(val)
            node.val = val

            if node.left: recover(node.left, val * 2 + 1)
            if node.right: recover(node.right, val * 2 + 2)

        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)