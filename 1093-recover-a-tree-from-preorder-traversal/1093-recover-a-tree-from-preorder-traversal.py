# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root = TreeNode()

        # Convert traversal order string to list of nodes
        nodes = []      # val, depth
        idx = 0
        val = ''

        while idx < len(traversal) and traversal[idx].isdigit():
            val += traversal[idx]
            idx += 1
        val = int(val)
        nodes.append([val, 0])

        while idx < len(traversal):
            depth = 0
            while idx < len(traversal) and traversal[idx] == '-':
                depth += 1
                idx += 1

            val = ''
            while idx < len(traversal) and traversal[idx].isdigit():
                val += traversal[idx]
                idx += 1
            val = int(val)

            nodes.append([val, depth])

        def recover(node, idx):
            val, depth = nodes[idx]
            node.val = val
            
            if idx + 1 == len(nodes):
                return node, idx

            if nodes[idx + 1][1] > depth:
                node.left, last_idx = recover(TreeNode(), idx + 1)

                if last_idx < len(nodes) - 1 and nodes[last_idx + 1][1] == depth + 1:
                    node.right, last_idx = recover(TreeNode(), last_idx + 1)

                return node, last_idx

            else:   # next_depth <= curr_depth
                return node, idx

        root, _ = recover(root, 0)

        return root
