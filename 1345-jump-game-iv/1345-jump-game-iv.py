class Solution:
    def minJumps(self, arr: List[int]) -> int:
        que = deque([[0, 0]])
        visit = [-1] * len(arr)
        visit[0] = 0
        dic = {}
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = [i]
            else:
                dic.get(arr[i]).append(i)
        S = set([])
        while que:
            pop = que.pop()
            if arr[pop[0]] not in S:
                S.add(arr[pop[0]])
                for linked in dic.get(arr[pop[0]]):
                    if pop[0] == linked:continue
                    if visit[linked] == -1:
                        visit[linked] = pop[1] + 1
                        que.appendleft([linked, pop[1] + 1])
            if pop[0] < len(arr) - 1 and visit[pop[0] + 1] == -1:
                visit[pop[0] + 1] = pop[1] + 1
                que.appendleft([pop[0] + 1, pop[1] + 1])
            if pop[0] > 0 and visit[pop[0] - 1] == -1:
                visit[pop[0] - 1] = pop[1] + 1
                que.appendleft([pop[0] - 1, pop[1] + 1])
        return visit[-1]
                