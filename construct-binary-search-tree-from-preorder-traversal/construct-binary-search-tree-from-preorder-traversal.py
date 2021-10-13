class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def makeTree(node, preorder, l, r, idx):
            if idx >= len(preorder) or r < preorder[idx] or preorder[idx] < l: return idx
            if preorder[idx] < node.val:
                nextNode = TreeNode(preorder[idx], None, None)
                node.left = nextNode
                idx = makeTree(nextNode, preorder, l, node.val, idx + 1)
            if idx >= len(preorder) or r < preorder[idx] or preorder[idx] < l: return idx
            if preorder[idx] > node.val:
                nextNode = TreeNode(preorder[idx], None, None)
                node.right = nextNode
                idx = makeTree(nextNode, preorder, node.val, r, idx + 1)
            return idx

        root = TreeNode(preorder[0], None, None)
        makeTree(root, preorder, 0, 10 ** 8 + 1, 1)
        return root