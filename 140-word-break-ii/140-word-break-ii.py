class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def recursion(p, s, res, setS, ans):
            if p == len(s):
                ans.append(res.strip())
                return
            w = ""
            temp = res
            for i in range(p, len(s)):
                w += s[i]
                if w in setS:
                    res += " " + w
                    recursion(i + 1, s, res, setS, ans)
                    res = temp

        setS = set(wordDict)
        ans = []
        recursion(0, s, "", setS, ans)
        return ans