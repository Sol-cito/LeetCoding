class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def search(cur, sumArr, ans):
            if not cur: return
            nArr = sumArr.copy()
            for i in range(len(nArr)):
                if cur.val + nArr[i] == targetSum: ans.append(cur)
                nArr[i] += cur.val
            nArr.append(cur.val)
            if cur.val == targetSum:ans.append(cur)
            search(cur.left, nArr, ans)
            search(cur.right, nArr, ans)
        
        ans = []
        search(root, [], ans)
        return len(ans)