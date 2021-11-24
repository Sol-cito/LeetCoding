class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        for f in firstList:
            a, b = f[0], f[1]
            for s in secondList:
                c, d = s[0], s[1]
                if b < c: break
                if d < a: continue
                ans.append([max(a, c), min(b, d)])
        return ans