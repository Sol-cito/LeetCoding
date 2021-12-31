# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, minVal, maxVal, res):
            if not node:return res
            res = max(abs(node.val - minVal), abs(node.val - maxVal), res)
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)
            r1 = dfs(node.left, minVal, maxVal, res)
            r2 = dfs(node.right, minVal, maxVal, res)
            return max(res, r1, r2)
        
        return dfs(root, root.val, root.val, 0)
            