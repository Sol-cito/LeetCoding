class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        arr = [1] * n
        ans = ""
        for i in reversed(range(len(arr))):
            if k > 0:
                r = min(k, 25)
                arr[i] += r
                k -= r
            ans += chr(arr[i] + 96)
        return ans[::-1]