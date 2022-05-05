class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(cur, arr, visitDic):
            if not cur:return
            arr.append(cur)
            visitDic[cur.val] = False
            dfs(cur.left, arr, visitDic)
            dfs(cur.right, arr, visitDic)
            
        def searchForest(cur, prev, res, S, visitDic):
            if not cur:
                return
            if cur.val in S:
                if cur == prev.left:
                    prev.left = None
                else:
                    prev.right = None
                return
                
            visitDic[cur.val] = True
            res.append(cur)
            searchForest(cur.left, cur, res, S, visitDic)
            searchForest(cur.right, cur, res, S, visitDic)
        
        arr = []
        visitDic = {}
        dfs(root, arr, visitDic)
        S = set(to_delete)
        ans = []
        for node in arr:
            if node.val not in S and not visitDic.get(node.val):
                ans.append(node)
                searchForest(node, None, [], S, visitDic)
        return ans
            