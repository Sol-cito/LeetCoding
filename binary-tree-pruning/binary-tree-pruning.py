class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def recursion(node):
            if not node: return 0
            l = recursion(node.left)
            if l == 0: node.left = None
            r = recursion(node.right)
            if r == 0: node.right = None
            return max(l, r, node.val)
        
        if recursion(root) == 0:return None
        return root