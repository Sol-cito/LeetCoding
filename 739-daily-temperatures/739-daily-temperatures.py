class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monostack = []
        ans = [0] * len(temperatures)
        for i in reversed(range(len(temperatures))):
            while monostack and monostack[-1][0] <= temperatures[i]:
                monostack.pop()
            if not monostack:
                ans[i] = 0
            else:
                ans[i] = monostack[-1][1] - i
            monostack.append([temperatures[i], i])
        return ans