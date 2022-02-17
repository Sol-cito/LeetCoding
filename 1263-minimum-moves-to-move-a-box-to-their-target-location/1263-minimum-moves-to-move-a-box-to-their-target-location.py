class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def isBoxNear(grid, sx, sy, bx, by, visit): # 박스가 person의 네 방향에 있는지 확인
            dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            for i in range(len(dir)):
                nx, ny = sx + dir[i][0], sy + dir[i][1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and nx == bx and ny == by:
                    return dir[i]
            return None
            
            
        def movePerson(grid, sx, sy, bx, by, visit): # 사람이 움직이면서 다음 턴 target을 return (sx, sy, bx, by)
            que = deque([[sx, sy]])
            S = set([grid[sx][sy]])
            res = []
            while que:
                pop = que.pop()
                r = isBoxNear(grid, pop[0], pop[1], bx, by, visit)
                if r:res.append(r)
                for x, y in [0, -1], [0, 1], [-1, 0], [1, 0]:
                    nx, ny = pop[0] + x, pop[1] + y
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not grid[nx][ny] in S and grid[nx][ny] != '#' and not (nx == bx and ny == by):
                        que.appendleft([nx, ny])
                        S.add(grid[nx][ny])
            return res
            
        
        sx, sy, bx, by, tx, ty = 0, 0, 0, 0, 0, 0
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '#': continue
                if grid[i][j] == 'B':
                    bx, by = i ,j
                elif grid[i][j] == 'S':
                    sx, sy = i, j
                elif grid[i][j] == 'T':
                    tx, ty = i, j
                grid[i][j] = num
                num +=1
        visit = [[False] * num for _ in range(num)] # 박스 / 사람
        
        que = deque([[sx, sy, bx, by, 0]])
        while que:
            pop = que.pop()
            r = movePerson(grid, pop[0], pop[1], pop[2], pop[3], visit)
            if pop[2] == tx and pop[3] == ty:return pop[4]
            for r1, r2 in r:
                nsx, nsy, nbx, nby = pop[2], pop[3], pop[2] + r1, pop[3] + r2
                if 0 <= nbx < len(grid) and 0 <= nby < len(grid[0]) and grid[nbx][nby] != '#' and not visit[grid[nsx][nsy]][grid[nbx][nby]]:
                    visit[grid[nsx][nsy]][grid[nbx][nby]] = True
                    que.appendleft([nsx, nsy, nbx, nby, pop[4] + 1])
        
        return -1             