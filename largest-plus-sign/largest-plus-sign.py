class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for ele in mines:
            grid[ele[0]][ele[1]] = 0
        arr = [[n] * n for _ in range(n)]
        ans = 0
        for i in range(n):
            sum = 0
            for j in range(n):
                sum = 0 if grid[i][j] == 0 else sum + 1
                arr[i][j] = min(arr[i][j], sum)
        for i in range(n):
            sum = 0
            for j in reversed(range(n)):
                sum = 0 if grid[i][j] == 0 else sum + 1
                arr[i][j] = min(arr[i][j], sum)
        for i in range(n):
            sum = 0
            for j in range(n):
                sum = 0 if grid[j][i] == 0 else sum + 1
                arr[j][i] = min(arr[j][i], sum)
        for i in range(n):
            sum = 0
            for j in reversed(range(n)):
                sum = 0 if grid[j][i] == 0 else sum + 1
                arr[j][i] = min(arr[j][i], sum)
                ans = max(ans, arr[j][i])
        return ans