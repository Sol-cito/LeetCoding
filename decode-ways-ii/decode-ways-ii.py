class Solution(object):
    def numDecodings(self, s):
        if s[0] == "0": return 0
        if len(s) == 1: return 9 if s == "*" else 1
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 9 if s[0] == "*" else 1
        for i in range(1, len(s)):
            if s[i] == "*":
                dp[i + 1] += dp[i] * 9 % (10 ** 9 + 7)
                if s[i - 1] == "*":
                    dp[i + 1] += dp[i - 1] * 15 % (10 ** 9 + 7)
                elif s[i - 1] == "1":
                    dp[i + 1] += dp[i - 1] * 9 % (10 ** 9 + 7)
                elif s[i - 1] == "2":
                    dp[i + 1] += dp[i - 1] * 6 % (10 ** 9 + 7)
            else:
                if s[i] != "0":
                    dp[i + 1] += dp[i]
                if s[i - 1] == "*":
                    if int(s[i]) <= 6:
                        dp[i + 1] += dp[i - 1] * 2 % (10 ** 9 + 7)
                    else:
                        dp[i + 1] += dp[i - 1] % (10 ** 9 + 7)
                elif 10 <= int(s[i - 1]) * 10 + int(s[i]) <= 26:
                    dp[i + 1] += dp[i - 1] % (10 ** 9 + 7)
        return dp[-1] % (10 ** 9 + 7)