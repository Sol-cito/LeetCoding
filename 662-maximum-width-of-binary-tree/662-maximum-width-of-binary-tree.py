class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque([[root, 0, 1]]) # cur, level, num
        ans = 1
        curLevel, left = 0, 1
        while que:
            pop = que.pop()
            if pop[1] > curLevel:
                curLevel = pop[1]
                left = pop[2]
            ans = max(ans, pop[2] - left + 1)
            if pop[0].left:
                que.appendleft([pop[0].left, pop[1] + 1, pop[2]*2 - 1])
            if pop[0].right:
                que.appendleft([pop[0].right, pop[1] + 1, pop[2]*2])
        return ans
             