class Solution:
    def find(self, node, p, q):
        if p.val > node.val and q.val > node.val:
            return self.find(node.right, p, q)
        elif p.val < node.val and q.val < node.val:
            return self.find(node.left, p, q)
        else:
            return node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p, q)