class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = set([])
        p, ans = 0, 0
        for i in range(len(s)):
            if s[i] not in t:
                t.add(s[i])
                ans = max(ans, len(t))
            else:
                while s[p] != s[i]:
                    t.remove(s[p])
                    p +=1
                p +=1
        return ans