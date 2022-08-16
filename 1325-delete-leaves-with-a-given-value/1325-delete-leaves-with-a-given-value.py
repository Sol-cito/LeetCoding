class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def search(cur):
            if not cur:return None
            cur.left = search(cur.left)
            cur.right = search(cur.right)
            if cur.val == target and not cur.left and not cur.right: return None
            return cur
        
        return search(root)