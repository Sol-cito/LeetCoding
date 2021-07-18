class Solution:
    def getDp(self, upperRow, curRow, dp):
        leftRes, rightRes = 0, 0
        for i in range(len(upperRow)):
            leftRes = max(leftRes, upperRow[i] - i)
            rightRes = max(rightRes, upperRow[len(upperRow) - 1 - i] - i)
        dp[0], dp[-1] = leftRes, rightRes
        for i in range(1, len(upperRow) - 1):
            dp[i] = max(upperRow[i], dp[i - 1] - 1, dp[i])
            dp[len(dp) - 1 - i] = max(upperRow[len(upperRow) - 1 - i], dp[len(dp) - i] - 1, dp[len(dp) - 1 - i])
        for i in range(len(curRow)):
            curRow[i] = curRow[i] + dp[i]
        return curRow

    def maxPoints(self, points) -> int:
        for i in range(1, len(points)):
            dp = [-1] * len(points[0])
            points[i] = self.getDp(points[i - 1], points[i], dp)
        return max(points[-1])