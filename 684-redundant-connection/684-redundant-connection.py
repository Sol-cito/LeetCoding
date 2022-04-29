class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def isAllConnected(dic, a, b, edges):
            visit = [False] * len(edges)
            que = deque([1])
            visit[0] = True
            cnt = 0
            while que:
                pop = que.pop()
                cnt += 1
                for link in dic.get(pop):
                    if not visit[link - 1] and not ((pop == a and link == b) or (pop == b and link == a)):
                        que.appendleft(link)
                        visit[link - 1] = True
            return cnt == len(edges)

        dic = dict(zip([i + 1 for i in range(len(edges))], [[] for _ in range(len(edges))]))
        for a, b in edges:
            dic.get(a).append(b)
            dic.get(b).append(a)
        for a, b in reversed(edges):
            if isAllConnected(dic, a, b, edges):
                return [a, b]