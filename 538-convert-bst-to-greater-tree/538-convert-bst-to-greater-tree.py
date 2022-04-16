class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def makeRight(cur):
            if not cur:return 0
            r = makeRight(cur.right)
            cur.val += r
            l = makeRight(cur.left)
            return cur.val + l
        
        def makeLeft(cur, p):
            if not cur:return
            cur.val += p
            makeLeft(cur.right, p)
            makeLeft(cur.left, cur.val)
            return 
            
        
        makeRight(root)
        makeLeft(root, 0)
        return root
            