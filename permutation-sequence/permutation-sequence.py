class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nArr = [i + 1 for i in range(n)]
        numArr = deque([1])
        num = 1
        for i in range(len(nArr) - 1):
            num *= nArr[i]
            numArr.appendleft(num)
        ans = ""
        for i in range(n):
            if k < numArr[i]:
                ans += str(nArr[0])
                del nArr[0]
                continue
            idx = math.ceil(k / numArr[i]) - 1
            ans += str(nArr[idx])
            k -= numArr[i] * idx
            del nArr[idx]
        return ans