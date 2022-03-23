class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def getNodes(cur, l):
            if not cur:return
            getNodes(cur.left, l)
            l.append(cur.val)
            getNodes(cur.right, l)
        
        l1, l2 = [], []
        getNodes(root1, l1)
        getNodes(root2, l2)
        ans = []
        p1, p2 = 0, 0
        while p1 < len(l1) or p2 < len(l2):
            if p2 == len(l2) or (p1 < len(l1) and l1[p1] <= l2[p2]):
                ans.append(l1[p1])
                p1 +=1
            elif p1 == len(l1) or (p2 < len(l2) and l1[p1] > l2[p2]):
                ans.append(l2[p2])
                p2 +=1
        return ans