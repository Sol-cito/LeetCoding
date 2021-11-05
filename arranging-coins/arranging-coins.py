class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt = 1
        while n >= cnt:
            n -= cnt
            cnt += 1
        return cnt - 1
