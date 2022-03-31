class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def search(node, total):
            if not node:return False
            if not node.left and not node.right:
                if total + node.val == targetSum:return True
                return False
            
            r1, r2 = False, False
            if node.left:
                r1 = search(node.left, total + node.val)
            if node.right:
                r2 = search(node.right, total + node.val)
            return r1 or r2
        
        
        if not root:return False
        return search(root, 0)