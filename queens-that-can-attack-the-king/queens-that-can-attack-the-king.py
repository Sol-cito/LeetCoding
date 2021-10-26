class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def checkDirection(dir, ans):
            dx, dy = king[0], king[1]
            while 0 <= dx < 9 and 0 <= dy < 9:
                if [dx, dy] in queens:
                    ans.append([dx, dy])
                    return
                dx += dir[0]
                dy += dir[1]

        ans = []
        for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]:
            checkDirection([dx, dy], ans)
        return ans
