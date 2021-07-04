class Solution(object):
    def countVowelPermutation(self, n):
        dp = [1] * 5
        for _ in range(n - 1):
            nDp = [0] * 5
            nDp[0] = dp[1] + dp[2] + dp[4]
            nDp[1] = dp[0] + dp[2]
            nDp[2] = dp[1] + dp[3]
            nDp[3] = dp[2]
            nDp[4] = dp[2] + dp[3]
            dp = nDp
        return sum(dp) % (10**9 + 7)
