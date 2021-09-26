class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visit = [[[False] * len(grid[0]) for _ in range(len(grid))] for _ in range(k + 1)]
        que = deque([[0, 0, k, 0]])
        ans = 1600
        while que:
            pop = que.pop()
            if pop[0] == len(grid) - 1 and pop[1] == len(grid[0]) - 1: ans = min(ans, pop[3])
            for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
                nx, ny = dx + pop[0], dy + pop[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 0 and not visit[pop[2]][nx][ny]:
                        visit[pop[2]][nx][ny] = True
                        que.appendleft([nx, ny, pop[2], pop[3] + 1])
                    if grid[nx][ny] == 1 and pop[2] > 0 and not visit[pop[2] - 1][nx][ny]:
                        visit[pop[2] - 1][nx][ny] = True
                        que.appendleft([nx, ny, pop[2] - 1, pop[3] + 1])
        return -1 if ans == 1600 else ans
