class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l, r = [0] * 26, [0] * 26
        S = set([])
        l[ord(s[0]) - 97] += 1
        for i in range(2, len(s)):
            r[ord(s[i]) - 97] += 1
        for i in range(1, len(s) - 1):
            for j in range(26):
                if l[j] > 0 and r[j] > 0:
                    S.add(chr(j + 97) + s[i] + chr(j + 97))
            l[ord(s[i]) - 97] += 1
            r[ord(s[i + 1]) - 97] -= 1
        return len(S)