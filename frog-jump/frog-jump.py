class Solution:
    def canCross(self, stones: List[int]) -> bool:
        S = [set([1])]
        for i in range(1, len(stones)):
            nSet = set([])
            for j in range(i):
                gap = stones[i] - stones[j]
                if gap in S[j]:
                    nSet.add(gap - 1)
                    nSet.add(gap)
                    nSet.add(gap + 1)
            S.append(nSet)
        if len(S[-1]) > 0:return True
        return False