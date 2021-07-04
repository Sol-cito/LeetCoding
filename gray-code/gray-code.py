class Solution(object):
    def grayCode(self, n):
        num = ['0'] * n
        S = set([0])
        ans = [0]
        while len(ans) < 2 ** n:
            for i in reversed(range(n)):
                num[i] = '0' if num[i] == '1' else '1'
                r = int("".join(num), 2)
                if r in S:
                    num[i] = '0' if num[i] == '1' else '1'
                    continue
                S.add(int(r))
                ans.append(int(r))
                break
        return ans
