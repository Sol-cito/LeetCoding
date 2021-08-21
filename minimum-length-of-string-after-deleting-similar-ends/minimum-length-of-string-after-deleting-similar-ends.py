class Solution:
    def minimumLength(self, s: str) -> int:
        p1, p2 = 0, len(s) - 1
        while p1 < p2 and s[p1] == s[p2]:
            while p1 < len(s) - 1 and s[p1] == s[p1 + 1]:p1 +=1
            while p2 > 0 and s[p2] == s[p2 - 1]: p2 -=1
            p1 +=1
            p2 -=1
        return max(0, p2 - p1 + 1)