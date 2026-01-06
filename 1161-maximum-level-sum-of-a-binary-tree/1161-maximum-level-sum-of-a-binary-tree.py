# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def bfs_with_level(root):
            # Edge case
            if root is None: return 1

            queue = deque([[root, 1]])
            max_level, curr_level = 1, 1
            max_sum = root.val
            curr_sum = 0

            while len(queue):
                node, level = queue.popleft()

                if level != curr_level:
                    # Record the level with maximum sum (hitherto)
                    if max_sum < curr_sum:
                        max_sum = curr_sum
                        max_level = curr_level

                    # Reset data for the next level
                    curr_level = level
                    curr_sum = 0
                
                curr_sum += node.val
                if node.left: queue.append((node.left, level + 1))
                if node.right: queue.append((node.right, level + 1))

            if max_sum < curr_sum: max_level = curr_level
                
            return max_level

        return bfs_with_level(root) 