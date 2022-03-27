class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [0] * len(pairs)
        dp[0] = 1
        ans = 1
        for i in range(1, len(pairs)):
            res = 1
            for j in range(i):
                if pairs[j][1] < pairs[i][0]: res = max(res, dp[j] + 1)
            dp[i] = res
            ans = max(ans, dp[i])
        return ans