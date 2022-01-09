class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        dirPointer = 0
        for l in instructions * 4:
            if l == 'G':
                x += dir[dirPointer][0]
                y += dir[dirPointer][1]
            elif l == 'L':
                dirPointer = (dirPointer + 1) % 4
            elif l == 'R':
                dirPointer = (dirPointer - 1) % 4
        return x == 0 and y == 0