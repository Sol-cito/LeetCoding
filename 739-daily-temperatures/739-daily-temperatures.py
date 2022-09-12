class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monostack = []
        ans = [0] * len(temperatures)
        for i in reversed(range(len(temperatures))):
            while monostack and temperatures[monostack[-1]] <= temperatures[i]:
                monostack.pop()
            if monostack:
                ans[i] = monostack[-1] - i
            monostack.append(i)
        return ans