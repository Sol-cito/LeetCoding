class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefixArr = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix))]
        self.matrix = matrix
        for i in range(len(self.matrix)):
            total = 0
            for j in range(len(self.matrix[0])):
                total += self.matrix[i][j]
                self.prefixArr[i][j + 1] = total
        return None
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            res += self.prefixArr[r][col2 + 1] - self.prefixArr[r][col1]
        return res
