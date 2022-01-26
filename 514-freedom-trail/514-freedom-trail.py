class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [[-1 for _ in range(len(ring))] for _ in range(len(key) + 1)]
        dp[0][0] = 0
        ans = len(ring) * len(key) + 1
        for i in range(len(key)):
            for j in range(len(ring)):
                if key[i] == ring[j]:
                    minVal = len(ring) * len(key) + 1
                    for k in range(len(ring)):
                        if dp[i][k] == -1:continue
                        if k <= j: 
                            length = min(j - k, len(ring) - j + k)
                        else:
                            length = min(k - j, len(ring) - k + j)
                        minVal = min(minVal, dp[i][k] + length)
                    dp[i + 1][j] = minVal
                    if i == len(key) - 1:
                        ans = min(ans, minVal)
        return ans + len(key)