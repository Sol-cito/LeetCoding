class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        ans = deque([[]])
        level = 0
        que = deque([[root, 0]])
        while que:
            pop = que.pop()
            if pop[1] > level:
                ans.appendleft([pop[0].val])
                level = pop[1]
            else:
                ans[0].append(pop[0].val)
            if pop[0].left:
                que.appendleft([pop[0].left, pop[1] + 1])
            if pop[0].right:
                que.appendleft([pop[0].right, pop[1] + 1])
        return ans