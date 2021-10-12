class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        que = deque([[root, 1]])
        ans = 10**5 + 1
        while que:
            pop = que.pop()
            if not pop[0].left and not pop[0].right:ans = min(ans, pop[1])
            if pop[0].left:que.appendleft([pop[0].left, pop[1] + 1])
            if pop[0].right:que.appendleft([pop[0].right, pop[1] + 1])
        return ans