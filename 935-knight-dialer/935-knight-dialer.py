class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        dials = [[1, 1, 1] for _ in range(4)]
        dials[3][0], dials[3][2] = 0, 0
        movements = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
        for i in range(n - 1):
            nDials = [[0, 0, 0] for _ in range(4)]
            for x in range(4):
                for y in range(3):
                    if (x == 3 and y == 0) or (x == 3 and y == 2): continue
                    for dx, dy in movements:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <= 3 and 0 <= ny <= 2 and not ((nx == 3 and ny == 0) or (nx == 3 and ny == 2)):
                            nDials[x][y] += dials[nx][ny]
            dials = nDials
        ans = 0
        for i in range(4):
            for j in range(3):
                ans += nDials[i][j]
        return ans % (10 ** 9 + 7)