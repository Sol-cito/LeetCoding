class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def recurse(cur, row, col, dic, colArr):
            if not cur:return
            if col in dic.keys():
                if row in dic.get(col).keys():
                    dic.get(col).get(row).append(cur.val)
                else:
                    dic.get(col)[row] = [cur.val]
            else:
                colArr.append(col)
                dic[col] = {row : [cur.val]}
            recurse(cur.left, row + 1, col - 1, dic, colArr)
            recurse(cur.right, row + 1, col + 1, dic, colArr)
            
        
        dic = {}
        colArr = []
        recurse(root, 0, 0, dic, colArr)
        colArr.sort()
        ans = []
        for col in colArr:
            res = []
            for rowKey in sorted(dic.get(col).keys()):
                for e in sorted(dic.get(col).get(rowKey)):
                    res.append(e)
            ans.append(res)
        return ans