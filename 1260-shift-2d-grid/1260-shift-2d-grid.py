class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ans = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x, y =  ((j + k) // len(grid[0]) + i) % len(grid), (j + k) % len(grid[0])
                ans[x][y] = grid[i][j]
        return ans
        