class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[-1] * len(mat[0]) for _ in range(len(mat))]
        que = deque([])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    que.appendleft([i, j, 1])
        while que:
            pop = que.pop()
            for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
                nx, ny = pop[0] + dx, pop[1] + dy
                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and ans[nx][ny] == -1:
                    ans[nx][ny] = pop[2]
                    que.appendleft([nx, ny, pop[2] + 1])
        return ans