class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        for t in timePoints:
            s = t.split(':')
            arr.append(int(s[0])*60 + int(s[1]))
        arr.sort()
        ans = 60 * 24 - arr[-1] + arr[0]
        for i in range(len(arr) - 1):
            ans = min(ans, arr[i + 1] - arr[i])
        return ans