class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def topDown(x, y, dp, amount):
            if dp[x][y] != -1:return dp[x][y]
            res = 0
            if y == 0:
                res = topDown(x - 1, y, dp, amount) / 2
            elif y == x:
                res = topDown(x - 1, y - 1, dp, amount) / 2
            else:
                res = topDown(x - 1, y, dp, amount) / 2 + topDown(x - 1, y - 1, dp, amount) / 2
            if res <= 1:
                amount[x][y] = res
                dp[x][y] = 0
            else:
                amount[x][y] = 1
                dp[x][y] = abs(1 - res)
            return dp[x][y]
        
        
        dp = [[-1] * 100 for _ in range(100)]
        amount = [[0] * 100 for _ in range(100)]
        dp[0][0] = abs(poured - 1) if poured > 1 else 0
        amount[0][0] = min(1, poured)
        topDown(query_row, query_glass, dp, amount)
        
        return amount[query_row][query_glass]