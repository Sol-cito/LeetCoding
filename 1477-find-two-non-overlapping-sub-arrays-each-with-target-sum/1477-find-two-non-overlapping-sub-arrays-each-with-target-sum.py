class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ans = len(arr) + 1
        p1, p2, total, minLeng = 0, 0, 0, len(arr) + 1
        minArr = [0] * len(arr)
        while p1 < len(arr):
            while p2 < len(arr) and total < target:
                total += arr[p2]
                minArr[p2] = minLeng
                p2 += 1
            if total == target:
                ans = min(ans, minArr[p1] + p2 - p1)
                minLeng = min(minLeng, p2 - p1)
            total -= arr[p1]
            p1 += 1
        return -1 if ans == len(arr) + 1 else ans
