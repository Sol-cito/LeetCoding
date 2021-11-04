class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def search(node, dir):
            if not node:return 0
            if not node.left and not node.right and dir == 0:return node.val
            r = search(node.left, 0) + search(node.right, 1)
            return r
        
        return search(root, -1)