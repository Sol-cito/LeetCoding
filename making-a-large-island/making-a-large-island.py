class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def findIslandAndMark(x, y, grid, visit, dir, landCnt):
            que = deque([[x, y]])
            toBeMarked = [[x, y]]
            maxArea = 0
            while que:
                pop = que.pop()
                maxArea += 1
                for dx, dy in dir:
                    nx, ny = pop[0] + dx, pop[1] + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visit[nx][ny] and grid[nx][ny] == 1:
                        que.appendleft([nx, ny])
                        visit[nx][ny] = True
                        toBeMarked.append([nx, ny])
            while toBeMarked:
                pop = toBeMarked.pop()
                grid[pop[0]][pop[1]] = [maxArea, landCnt]
            return maxArea

        visit = [[False] * len(grid[0]) for _ in range(len(grid))]
        dir = [1, 0], [0, 1], [-1, 0], [0, -1]
        water = []
        landCnt = 1
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = [0, 0]
                    water.append([i, j])
                elif grid[i][j] == 1 and not visit[i][j]:
                    visit[i][j] = True
                    ans = max(ans, findIslandAndMark(i, j, grid, visit, dir, landCnt))
                    landCnt += 1
        for i, j in water:
            landCntBox = []
            res = 1
            for dx, dy in dir:
                nx, ny = dx + i, dy + j
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny][1] > 0:
                    if grid[nx][ny][1] not in landCntBox:
                        landCntBox.append(grid[nx][ny][1])
                        res += grid[nx][ny][0]
            ans = max(ans, res)
        return ans
