class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def recursion(node, dic):
            if not node: return 0
            dic[node] = recursion(node.left, dic) + recursion(node.right, dic) + node.val
            return dic.get(node)

        dic = {}
        recursion(root, dic)
        ans = 0
        for eachNode in dic.keys():
            ans = max(ans, (dic.get(root) - dic.get(eachNode)) * dic.get(eachNode))
        return ans % (10**9 + 7)