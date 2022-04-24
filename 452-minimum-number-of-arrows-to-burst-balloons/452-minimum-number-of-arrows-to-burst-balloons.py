class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        l, r = points[0][0], points[0][1]
        ans = 1
        for i in range(1, len(points)):
            if points[i][0] > r:
                l = points[i][0]
                r = points[i][1]
                ans +=1
            else:
                l = min(l, points[i][0])
                r = min(r, points[i][1])
        return ans