class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:return True
        p = 0
        for l in t:
            if s[p] == l:
                p +=1
            if p == len(s):return True
        return False