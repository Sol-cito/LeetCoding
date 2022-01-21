class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def fillDp(num, dp, cnt):
            if dp[num - 1] != -1: return dp[num - 1]
            if num % 2 == 0:
                res = fillDp(num // 2, dp, cnt + 1)
            else:
                res = fillDp(3 * num + 1, dp, cnt + 1)
            dp[num - 1] = res + 1
            return res + 1

        dp = [-1] * 260000
        dp[0] = 0
        for i in range(1, 1000):
            fillDp(i, dp, 0)
        heap = []
        for i in range(lo, hi + 1):
            heapq.heappush(heap, [dp[i - 1], i])
        cnt = 0
        while cnt < k - 1:
            heapq.heappop(heap)
            cnt += 1
        return heapq.heappop(heap)[1]