class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        hor, ver = [0] * m, [0] * n
        for a, b in ops:
            hor[a - 1] += 1
            ver[b - 1] += 1
        a, b = m, n
        for i in reversed(range(len(hor))):
            if hor[i] != 0: a = i + 1
        for i in reversed(range(len(ver))):
            if ver[i] != 0: b = i + 1
        return a * b