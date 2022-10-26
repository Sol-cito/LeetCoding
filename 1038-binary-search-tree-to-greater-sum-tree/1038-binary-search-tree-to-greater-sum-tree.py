class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def recurse(cur, sum):
            if not cur: return 0
            temp = cur.val
            r1 = recurse(cur.right, sum)
            cur.val += r1 + sum
            r2 = recurse(cur.left, cur.val)
            return temp + r1 + r2

        root.val += recurse(root.right, 0)
        recurse(root.left, root.val)
        return root
