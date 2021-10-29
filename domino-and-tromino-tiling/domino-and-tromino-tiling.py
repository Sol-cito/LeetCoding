class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:return 1
        dp = [[0] * (n + 1) for _ in range(5)]
        dp[0][0], dp[0][1] = 1, 1
        for i in range(2, n + 1):
            dp[0][i] = dp[0][i - 1] + dp[1][i - 1] + dp[4][i - 1]
            dp[1][i] = dp[0][i - 2] + dp[1][i - 2] + dp[4][i - 2]
            dp[2][i] = dp[3][i - 1] + dp[0][i - 2] + dp[1][i - 2] + dp[4][i - 2]
            dp[3][i] = dp[2][i - 1] + dp[0][i - 2] + dp[1][i - 2] + dp[4][i - 2]
            dp[4][i] = dp[2][i - 1] + dp[3][i - 1]
        return (dp[0][n] + dp[1][n] + dp[4][n]) % (10**9 + 7)
