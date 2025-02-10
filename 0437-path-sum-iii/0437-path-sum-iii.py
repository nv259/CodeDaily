# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        
        count_prefixsum = {0: 1} 
        self.res = 0

        def dfs(node, curr_sum):
            # print(node.val, curr_sum)
            if curr_sum - targetSum in count_prefixsum:
                self.res += count_prefixsum[curr_sum - targetSum]

            if curr_sum not in count_prefixsum:
                count_prefixsum[curr_sum] = 1
            else:
                count_prefixsum[curr_sum] += 1

            if node.left:
                dfs(node.left, curr_sum + node.left.val)
            if node.right: 
                dfs(node.right, curr_sum + node.right.val)

            count_prefixsum[curr_sum] -= 1
            if count_prefixsum[curr_sum] == 0: 
                del count_prefixsum[curr_sum] 

            return 0            

        dfs(root, root.val)

        return self.res