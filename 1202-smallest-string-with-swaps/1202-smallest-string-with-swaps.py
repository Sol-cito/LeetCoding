class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def bfs(idx, s, dic, visit):
            que = deque([idx])
            alphaRes, idxRes = [], []
            while que:
                pop = que.pop()
                alphaRes.append(s[pop])
                idxRes.append(pop)
                for l in dic.get(pop):
                    if not visit[l]:
                        visit[l] = True
                        que.appendleft(l)
            return [sorted(alphaRes), sorted(idxRes)]

        dic = dict(zip([i for i in range(len(s))], [set([]) for _ in range(len(s))]))
        for a, b in pairs:
            dic.get(a).add(b)
            dic.get(b).add(a)
        visit = [False] * len(s)
        ans = [0] * len(s)
        for i in range(len(s)):
            if not visit[i]:
                visit[i] = True
                r = bfs(i, s, dic, visit)
                for j in range(len(r[0])):
                    ans[r[1][j]] = r[0][j]
        return "".join(ans)