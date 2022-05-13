class Solution:
    def connect(self, root: 'Node') -> 'Node':
        que = deque([[root, 0]])
        prev = [None, -1]
        while que:
            pop = que.pop()
            if prev[0] and pop[1] == prev[1]:
                prev[0].next = pop[0]
            if pop[0] and pop[0].left:
                que.appendleft([pop[0].left, pop[1] + 1])
            if pop[0] and pop[0].right:
                que.appendleft([pop[0].right, pop[1] + 1])
            prev = pop
        return root