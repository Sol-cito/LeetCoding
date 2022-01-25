class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def search(cur, target, steps):
            if not cur:return None
            if cur == target:return steps
            steps.append('l')
            l = search(cur.left, target, steps.copy())
            if l:return l
            del steps[-1]
            steps.append('r')
            r = search(cur.right, target, steps.copy())
            if r:return r
            return None
        
        steps = search(original, target, [])
        ans = cloned
        for ele in steps:
            if ele == 'l':
                ans = ans.left
            else:
                ans = ans.right
        return ans