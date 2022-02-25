class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(p)):
            nDp = [0] * (len(s) + 1)
            if p[i] == "*":
                startIdx = -1
                for j in range(len(dp)):
                    if dp[j] == 1:
                        startIdx = j
                        break
                if startIdx > -1:
                    for j in range(startIdx, len(dp)):
                        nDp[j] = 1
                dp = nDp
                continue
            for j in range(1, len(dp)):
                if p[i] == "?":
                    if dp[j - 1] == 1:
                        nDp[j] = 1
                else:
                    if dp[j - 1] == 1 and p[i] == s[j - 1]:
                        nDp[j] = 1
            dp = nDp
        return dp[-1] == 1