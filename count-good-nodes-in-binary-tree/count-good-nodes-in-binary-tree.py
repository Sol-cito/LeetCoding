class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recursion(node, maxValue):
            if not node: return 0
            res = 0
            if node.val >= maxValue: res += 1
            res += recursion(node.left, max(node.val, maxValue)) + \
                  recursion(node.right, max(node.val, maxValue))
            return res

        return recursion(root, -(10 ** 4))