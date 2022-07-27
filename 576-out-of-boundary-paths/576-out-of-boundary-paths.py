class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def topDown(r, c, move, dp):
            if dp[move][r][c] != -1: return dp[move][r][c]
            if move == 0: return 0
            res = 0
            for dx, dy in dir:
                nx, ny = r + dx, c + dy
                if 0 <= nx < m and 0 <= ny < n:
                    res += topDown(nx, ny, move - 1, dp)
            dp[move][r][c] = res
            return res
        
        if maxMove == 0: return 0
        dp = [[[-1] * n for _ in range(m)] for _ in range(maxMove)]
        dp[0][startRow][startColumn] = 1
        ans = 0
        for i in range(m):
            for j in range(n):
                topDown(i, j, maxMove - 1, dp)

        for i in range(m):
            for move in range(maxMove):
                ans += max(0, dp[move][i][0]) + max(0, dp[move][i][n - 1])
        for i in range(n):
            for move in range(maxMove):
                ans += max(0, dp[move][0][i]) + max(0, dp[move][m - 1][i])
        return ans % (10 ** 9 + 7)