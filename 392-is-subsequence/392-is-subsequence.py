class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tlist = list(t)
        for l in s:
            if l in tlist:
                tlist = tlist[tlist.index(l) + 1:]
                print(tlist)
            else:return False
        return True