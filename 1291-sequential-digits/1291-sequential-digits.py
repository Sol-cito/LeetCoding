class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def recursion(cur, targetLen, low, high, ans):
            if len(cur) == targetLen:
                if low <= int(cur) <= high: ans.append(int(cur))
                return
            if cur[-1] == "9": return
            recursion(cur + str(int(cur[-1]) + 1), targetLen, low, high, ans)

        ans = []
        for targetLen in range(len(str(low)), len(str(high)) + 1):
            for i in range(1, 10):
                recursion(str(i), targetLen, low, high, ans)
        return ans