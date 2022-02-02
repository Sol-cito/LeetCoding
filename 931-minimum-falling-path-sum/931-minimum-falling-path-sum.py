class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def goDp(matrix, dp, x, y):
            if x == 0:return matrix[x][y]
            if dp[x][y] > -(101 * 101):return dp[x][y]
            minVal = 101 * 101
            for dy in [-1, 0, 1]:
                if y + dy < 0 or y + dy > len(matrix) - 1:continue
                minVal = min(minVal, matrix[x][y] + goDp(matrix, dp, x - 1, y + dy))
            dp[x][y] = minVal
            return minVal
                
        dp = [[-(101 * 101)] * len(matrix) for _ in range(len(matrix))]
        ans = 101 * 101
        for i in range(len(matrix)):
            ans = min(ans, goDp(matrix, dp, len(matrix) - 1, i))
        return ans