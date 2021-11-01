class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(x, y, board, visit):
            que = deque([[x, y]])
            isSurrounded = True
            nQue = deque([])
            while que:
                pop = que.pop()
                if pop[0] == 0 or pop[0] == len(board) - 1 or pop[1] == 0 or pop[1] == len(
                        board[0]) - 1: isSurrounded = False
                nQue.appendleft(pop)
                for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
                    nx, ny = dx + pop[0], dy + pop[1]
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and not visit[nx][ny] and board[nx][ny] == 'O':
                        visit[nx][ny] = True
                        que.appendleft([nx, ny])
            if isSurrounded:
                while nQue:
                    pop = nQue.pop()
                    board[pop[0]][pop[1]] = 'X'

        visit = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not visit[i][j] and board[i][j] == 'O':
                    visit[i][j] = True
                    bfs(i, j, board, visit)