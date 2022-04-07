class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a == b == 0:return ""
        if a == 0: return "b"*b
        if b == 0:return "a"*a
        r = max(a, b)
        if a >= b:
            l, s = "a", "b"
        else:
            l, s = "b", "a"
        ans = ""
        for _ in range(min(a, b)):
            ans += l + s
        r -= min(a, b)
        while r > 0:
            flag = False
            for i in range(len(ans) - 2):
                if ans[i:i + 3] == s + l + s:
                    flag = True
                    ans = ans[:i + 1] + l + ans[i + 1:]
                    r -=1
                    break
            if not flag:break
        while r > 0:
            if ans[0] == s or (len(ans) > 1 and ans[1] == s):
                ans = l + ans
            else:
                ans = ans + l
            r -=1
        return ans
        