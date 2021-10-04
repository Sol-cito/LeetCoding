class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node: return [], 0
            if not node.left and not node.right: return [0], 0
            left, lr = dfs(node.left)
            right, rr = dfs(node.right)
            res = 0
            nArr = []
            for nl in left:
                for nr in right:
                    if nl + nr + 2 <= distance:
                        res += 1
            for nl in left: nArr.append(nl + 1)
            for nr in right: nArr.append(nr + 1)
            return nArr, lr + rr + res

        return dfs(root)[1]