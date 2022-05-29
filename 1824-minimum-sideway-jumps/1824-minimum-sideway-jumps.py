class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        M = 5 * 10 ** 6
        dp = [1, 0, 1]
        for i in range(len(obstacles)):
            nDp = [0, 0, 0]
            for j in range(3):
                nDp[j] = min(dp[j], min(dp) + 1)
            if obstacles[i] > 0: nDp[obstacles[i] - 1] = M
            if nDp[0] != M: nDp[0] = min(dp[0], nDp[1] + 1, nDp[2] + 1)
            if nDp[1] != M: nDp[1] = min(dp[1], nDp[0] + 1, nDp[2] + 1)
            if nDp[2] != M: nDp[2] = min(dp[2], nDp[0] + 1, nDp[1] + 1)
            dp = nDp
        return min(dp)