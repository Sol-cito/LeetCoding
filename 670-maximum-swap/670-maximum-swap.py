class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(map(lambda x: str(x), str(num)))
        ans = num
        for i in range(len(arr) - 1):
            maxNum, idx = int(arr[i]), i
            for j in reversed(range(i + 1, len(arr))):
                if maxNum < int(arr[j]):
                    maxNum = max(maxNum, int(arr[j]))
                    idx = j
            if maxNum > int(arr[i]):
                l = str(num)
                ans = max(ans, int(l[:i] + arr[idx] + l[i + 1:idx] + arr[i] + l[idx + 1:]))
        return ans