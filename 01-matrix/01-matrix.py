class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def topDown(x, y, dp, mat, dir):
            if dp[x][y] != -1: return dp[x][y]
            if mat[x][y] == 0:
                dp[x][y] = 0
                return 0
            res = 10 ** 4
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
                    res = min(res, topDown(nx, ny, dp, mat, dir) + 1)
            dp[x][y] = res
            return res

        def topDown2(x, y, dp1, dp2, mat, dir):
            if dp2[x][y] != -1: return dp2[x][y]
            if mat[x][y] == 0:
                dp2[x][y] = 0
                return 0
            res = dp1[x][y]
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
                    res = min(res, topDown2(nx, ny, dp1, dp2, mat, dir) + 1)
            dp2[x][y] = res
            return dp2[x][y]

        dp1 = [[-1] * len(mat[0]) for _ in range(len(mat))]
        dp2 = [[-1] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                topDown(i, j, dp1, mat, [[0, 1], [1, 0]])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                topDown2(i, j, dp1, dp2, mat, [[0, -1], [-1, 0]])
        return dp2