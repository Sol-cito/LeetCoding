class Solution(object):
    def countVowelPermutation(self, n):
        dp = [[1] * 5]
        for _ in range(n - 1):
            nDp = [0] * 5
            nDp[0] = dp[-1][1] + dp[-1][2] + dp[-1][4]
            nDp[1] = dp[-1][0] + dp[-1][2]
            nDp[2] = dp[-1][1] + dp[-1][3]
            nDp[3] = dp[-1][2]
            nDp[4] = dp[-1][2] + dp[-1][3]
            dp.append(nDp)
        return sum(dp[-1]) % (10**9 + 7)
