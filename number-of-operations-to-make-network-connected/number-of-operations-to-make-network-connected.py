class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def bfs(start, comDic, visit):
            que = deque([start])
            while que:
                pop = que.pop()
                for linked in comDic.get(pop):
                    if not visit[linked]:
                        visit[linked] = True
                        que.appendleft(linked)
            return            
        
        if len(connections) < n - 1:return -1
        comDic = dict(zip([i for i in range(n)], [[] for _ in range(n)]))
        for pair in connections:
            comDic.get(pair[0]).append(pair[1])
            comDic.get(pair[1]).append(pair[0])
        visit = [False] * n
        
        cnt = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                bfs(i, comDic, visit)
                cnt +=1
        return cnt - 1
        