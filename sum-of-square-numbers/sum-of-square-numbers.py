class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        S = set([0])
        num = 1
        while num * num <= 2 ** 31 - 1:
            S.add(num * num)
            num += 1
        for ele in S:
            if c - ele in S: return True
        return False