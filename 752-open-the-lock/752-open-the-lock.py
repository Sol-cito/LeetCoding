class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def makePlusNum(arr, idx):
            arr[idx] = str((int(arr[idx]) + 1) % 10)
            return arr[0] + arr[1] + arr[2] + arr[3]

        def makeMinusNum(arr, idx):
            arr[idx] = "9" if arr[idx] == "0" else str(int(arr[idx]) - 1)
            return arr[0] + arr[1] + arr[2] + arr[3]

        S = set(deadends)
        if "0000" in S: return -1
        visit = set([])
        que = deque([["0000", 0]])
        while que:
            pop = que.pop()
            if pop[0] == target: return pop[1]
            for i in range(4):
                pn, mn = makePlusNum([pop[0][0], pop[0][1], pop[0][2], pop[0][3]], i), makeMinusNum(
                    [pop[0][0], pop[0][1], pop[0][2], pop[0][3]], i)
                if pn not in S and pn not in visit:
                    visit.add(pn)
                    que.appendleft([pn, pop[1] + 1])
                if mn not in S and mn not in visit:
                    visit.add(mn)
                    que.appendleft([mn, pop[1] + 1])
        return -1
    