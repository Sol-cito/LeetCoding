class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        for n in nums:
            if len(arr) == 0 or arr[-1][0] != n:
                arr.append([n, 1])
            else:
                arr[-1][1] += 1
        dp = [arr[0][0] * arr[0][1], 0]
        for i in range(1, len(arr)):
            nDp = [0, 0]
            if arr[i - 1][0] != arr[i][0] - 1:
                nDp[0] = max(dp) + arr[i][0] * arr[i][1]
            else:
                nDp[0] = dp[1] + arr[i][0] * arr[i][1]
            nDp[1] = max(dp)
            dp = nDp
        return max(dp)