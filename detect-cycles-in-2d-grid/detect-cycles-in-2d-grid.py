class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def search(prev, x, y, visit, grid, dir, cnt, visitCnt):
            for dx, dy in dir:
                nx, ny = dx + x, dy + y
                if 0 <= nx < len(grid) and 0<= ny < len(grid[0]) and grid[nx][ny] == grid[x][y]:
                    if visit[nx][ny] == visitCnt and (nx != prev[0] or ny != prev[1]) and cnt >= 4: return True
                    if visit[nx][ny] == -1:
                        visit[nx][ny] = visitCnt
                        if search([x, y], nx, ny, visit, grid, dir, cnt + 1, visitCnt):return True
            return False
                        
                        
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = [[-1] * len(grid[0]) for _ in range(len(grid))]
        visitCnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visit[i][j] == -1:
                    visit[i][j] = visitCnt
                    if search([-1, -1], i, j, visit, grid, dir, 1, visitCnt):return True
                    visitCnt +=1
        return False