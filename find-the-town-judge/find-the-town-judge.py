class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree, outDegree = [0] * n, [0] * n
        for a, b in trust:
            inDegree[b - 1] +=1
            outDegree[a - 1] +=1
        judgeByOutdegree, judgeByIndegree = [], []
        for i in range(n):
            if outDegree[i] == 0: judgeByOutdegree.append(i + 1)
            if inDegree[i] == n - 1: judgeByIndegree.append(i + 1)
        if len(judgeByOutdegree) == len(judgeByIndegree) and judgeByOutdegree[0] == judgeByIndegree[0]: return judgeByOutdegree[0]
        return -1