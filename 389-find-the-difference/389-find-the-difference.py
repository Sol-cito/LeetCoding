class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alpha = [0] * 26
        for l in s:
            alpha[ord(l) - 97] +=1
        for l in t:
            if alpha[ord(l) - 97] == 0:return l
            alpha[ord(l) - 97] -=1