class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        arr = [[0] * n for _ in range(n)]
        for x, y in roads:
            arr[x][y] = arr[y][x] = 1
        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j: continue
                ans = max(ans, sum(arr[i]) + sum(arr[j]) - arr[i][j])
        return ans
