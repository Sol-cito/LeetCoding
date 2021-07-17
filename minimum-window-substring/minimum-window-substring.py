class Solution:
    def getIdx(self, dic, S, s):
        minIdx, maxIdx = 10 ** 5 + 1, 0
        for l in S:
            minIdx = min(minIdx, dic.get(ord(l) - 65)[0])
            maxIdx = max(maxIdx, dic.get(ord(l) - 65)[-1])
        return s[minIdx:maxIdx + 1]

    def minWindow(self, s: str, t: str) -> str:
        ans, foundFlag = s, False
        S, alpha = set(t), [0] * 60
        for l in t:
            alpha[ord(l) - 65] += 1
        dic = dict(zip([i for i in range(60)], [[] for _ in range(60)]))
        cnt = 0
        for i in range(len(s)):
            if s[i] not in S: continue
            if len(dic.get(ord(s[i]) - 65)) < alpha[ord(s[i]) - 65]:
                dic.get(ord(s[i]) - 65).append(i)
                cnt += 1
            else:
                del dic.get(ord(s[i]) - 65)[0]
                dic.get(ord(s[i]) - 65).append(i)
            if cnt == len(t):
                sub = self.getIdx(dic, S, s)
                foundFlag = True
                if len(sub) < len(ans):
                    ans = sub
        return ans if foundFlag else ""