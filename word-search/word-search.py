class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, i, j, cnt, word, visit):
            if cnt == len(word): return True
            if cnt > len(word): return False

            for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == word[cnt] and not \
                        visit[nx][ny]:
                    visit[nx][ny] = True
                    if dfs(board, nx, ny, cnt + 1, word, visit): return True
                    visit[nx][ny] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                visit = [[False] * len(board[0]) for _ in range(len(board))]
                visit[i][j] = True
                if board[i][j] == word[0] and dfs(board, i, j, 1, word, visit): return True
        return False