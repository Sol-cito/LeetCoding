class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic, S = {}, set([])
        for i in range(len(s)):
            if s[i] not in dic.keys() and t[i] not in S:
                dic[s[i]] = t[i]
                S.add(t[i])
            elif s[i] not in dic.keys() and t[i] in S:
                return False
            elif s[i] in dic.keys() and t[i] not in S:
                return False
            elif s[i] in dic.keys() and dic.get(s[i]) != t[i]:
                return False
        return True