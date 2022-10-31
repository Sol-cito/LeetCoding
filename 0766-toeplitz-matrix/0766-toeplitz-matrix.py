class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def helper(a, b):
            num = matrix[a][b]
            while 0 <= a < len(matrix) and 0 <= b < len(matrix[0]):
                if num != matrix[a][b]:return False
                a +=1
                b +=1
            return True
        
        for i in range(len(matrix[0]) - 1):
            if not helper(0, i): return False
        for i in range(1, len(matrix)):
            if not helper(i, 0): return False
        return True