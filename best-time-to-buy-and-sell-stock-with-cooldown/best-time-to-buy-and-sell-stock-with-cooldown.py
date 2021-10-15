class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0, 0]]
        buy, sell, coll = 0, 0, 0
        ans = 0
        for i in range(1, len(prices)):
            nDp = [0, 0, 0]
            for j in range(len(dp)):
                if j == len(dp) - 1:
                    nDp[0] = max(nDp[0], dp[j][2])
                else:
                    nDp[0] = max(nDp[0], dp[j][1], dp[j][2])
                nDp[1] = max(nDp[1], dp[j][0] + prices[i] - prices[j])
            nDp[2] = dp[i - 1][1]
            dp.append(nDp)
            ans = max(ans, nDp[0], nDp[1], nDp[2])
        return ans