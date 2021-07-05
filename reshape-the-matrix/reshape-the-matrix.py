class Solution(object):
    def matrixReshape(self, mat, r, c):
        if len(mat) * len(mat[0]) != r * c: return mat
        ans, x, y = [[0] * c for _ in range(r)], 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[x][y] = mat[i][j]
                if y < c - 1:
                    y += 1
                else:
                    y = 0
                    x += 1
        return ans