class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt = 0
                    for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
                        if 0 <= dx + i < len(grid) and 0 <= dy + j < len(grid[0]) and grid[dx + i][dy + j] == 1:
                            cnt += 1
                    ans += 4 - cnt
        return ans
