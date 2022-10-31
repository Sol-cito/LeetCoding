class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        oneRow = matrix[0]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if oneRow[j - 1] != matrix[i][j]: return False
            oneRow = matrix[i]
        return True