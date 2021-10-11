# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def search(node, ans):
            if not node: return -1001
            l, r = search(node.left, ans), search(node.right, ans)
            ans[0] = max(ans[0], node.val, l, r, node.val + l, node.val + r, node.val + r + l)
            return max(node.val, node.val + l, node.val + r)
            
        ans = [-1001]
        search(root, ans)
        return ans[0]