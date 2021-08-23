# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(S, node):
            if not node:return
            S.add(node.val)
            dfs(S, node.left)
            dfs(S, node.right)
        
        S = set([])
        dfs(S, root)
        for ele in S:
            if ele * 2 != k and k - ele in S:return True
        return False
        