class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def checkNum(board, x, y, num):
            for i in range(9):
                if board[x][i] == num or board[i][y] == num:return False
            for i in range(3):
                for j in range(3):
                    if board[x//3 * 3 + i][y // 3 * 3 + j] == num:return False
            return True
        
        
        def backtracking(board, curCnt, cnt):
            if curCnt == cnt:return True
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":continue
                    for num in range(1, 10):
                        if checkNum(board, i, j, str(num)):
                            board[i][j] = str(num)
                            if backtracking(board, curCnt + 1, cnt):
                                return True
                            board[i][j] = "."
                    return False
            return False                      
                       
        cnt = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":cnt +=1
        backtracking(board, 0, cnt)
        
                            
        