class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(position, dp):
            if dp[position] != -1:return dp[position]
            res = climb(position - 1, dp) + climb(position - 2, dp)
            dp[position] = res
            return res
        
        dp = [-1] * (n + 1)
        dp[0] = dp[1] = 1
        return climb(n, dp)