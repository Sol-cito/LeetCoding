class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque([])
        visit = [[False] * len(grid[0]) for _ in range(len(grid))]
        freshCnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    visit[i][j] = True
                    que.appendleft([i, j, 0])
                elif grid[i][j] == 1:
                    freshCnt +=1
        howMany = 0
        while que:
            pop = que.pop()
            howMany = max(howMany, pop[2])
            for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
                nx, ny = pop[0] + dx, pop[1] + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visit[nx][ny] and grid[nx][ny] == 1:
                    freshCnt -= 1
                    que.appendleft([nx, ny, pop[2] + 1])
                    visit[nx][ny] = True
        if freshCnt > 0:return -1
        return howMany
        
