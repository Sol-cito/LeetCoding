class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans, sumNum, cnt = 1, 1, 2
        while sumNum < n:
            if sumNum % cnt == n % cnt: ans += 1
            sumNum += cnt
            cnt += 1
        return ans