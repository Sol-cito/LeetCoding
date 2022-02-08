class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [[0] * len(days) for _ in range(3)]
        dp[0][0] = min(costs)
        dp[1][0], dp[2][0] = costs[1], costs[2]
        for i in range(1, len(days)):
            minVal = 100000 * 365
            for j in reversed(range(i)):
                diff = days[i] - days[j]
                if diff >= 30:break
                if 1 <= diff <= 6:
                    minVal = min(minVal, dp[1][j], dp[2][j])
                if 7 <= diff <= 29:
                    minVal = min(minVal, dp[2][j])
            dp[0][i] = min(dp[0][i - 1] + min(costs), minVal)
            dp[1][i] = dp[0][i - 1] + costs[1]
            dp[2][i] = dp[0][i - 1] + costs[2]
        print(dp)
        return dp[0][-1]