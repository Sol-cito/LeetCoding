class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def check(x, y, visit):
            dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            canWalkOff = False
            cnt = 0
            que = deque([[x, y]])
            while que:
                pop = que.pop()
                cnt +=1
                for dx, dy in dir:
                    nx, ny = pop[0] + dx, pop[1] + dy
                    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):canWalkOff = True
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and not visit[nx][ny]:
                        visit[nx][ny] = True
                        que.appendleft([nx, ny])
            return [canWalkOff, cnt]
        
        
        visit = [[False] * len(grid[0]) for _ in range(len(grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visit[i][j]:
                    visit[i][j] = True
                    res = check(i, j, visit)
                    if not res[0]: ans += res[1]
        return ans