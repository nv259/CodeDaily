# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            deepest_left_node = None
            deepest_left_level = -1
            deepest_right_node = None

            queue = deque([(root, 0)])

            while len(queue):
                node, level = queue.popleft()

                if level > deepest_left_level: 
                    deepest_left_node = node
                    deepest_left_level = level
                    deepest_right_node = None
                elif level == deepest_left_level:
                    deepest_right_node = node
                
                if node.left: 
                    node.left.parent = node
                    queue.append((node.left, level + 1))
                if node.right: 
                    node.right.parent = node 
                    queue.append((node.right, level + 1))
            
            return deepest_left_node, deepest_right_node, deepest_left_level
        
        # LCA of two nodes of the same level
        def lca(x, y):
            if x.parent == y.parent:
                return x.parent
            return lca(x.parent, y.parent)

        deepest_left_node, deepest_right_node, deepest_level = bfs(root)
        if not deepest_right_node:
            return deepest_left_node
        return lca(deepest_left_node, deepest_right_node)