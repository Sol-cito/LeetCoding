class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def recursion(node, res, sum, ans):
            if not node: return
            res.append(node.val)
            if not node.left and not node.right and sum + node.val == targetSum:ans.append(res.copy())
            recursion(node.left, res, sum + node.val, ans)
            recursion(node.right, res, sum + node.val, ans)
            del res[-1]
                
        if not root: return []
        ans = []
        recursion(root, [], 0, ans)
        return ans