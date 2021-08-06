"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        ans = []
        que = deque([root])
        cnt = 1
        while que:
            res, nextCnt = [], 0
            for i in range(cnt):
                pop = que.pop()
                res.append(pop.val)
                for child in pop.children:
                    if not child: continue
                    que.appendleft(child)
                    nextCnt += 1
            ans.append(res)
            cnt = nextCnt
        return ans