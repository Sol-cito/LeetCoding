class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def calculate(res, target):
            arr = []
            r = ""
            for ele in res:
                if ele not in ["*", "+", "-"]:
                    r += ele
                else:
                    if len(r) > 1 and r[0] == "0":return target - 1
                    arr.append(int(r))
                    arr.append(ele)
                    r = ""
            if len(r) > 1 and r[0] == "0": return target - 1
            arr.append(int(r))
            stack = []
            p = 0
            while p < len(arr):
                if arr[p] != "*":
                    stack.append(arr[p])
                else:
                    stack.append(stack.pop() * arr[p + 1])
                    p += 1
                p += 1
            r = stack[0]
            for i in range(1, len(stack), 2):
                if stack[i] == '+':
                    r += stack[i + 1]
                else:
                    r -= stack[i + 1]
            return r

        def recursion(num, p, res, target, ans):
            if p == len(num):
                r = calculate(res, target)
                if r == target: ans.append(res)
                return
            recursion(num, p + 1, res + num[p], target, ans)
            recursion(num, p + 1, res + "+" + num[p], target, ans)
            recursion(num, p + 1, res + "-" + num[p], target, ans)
            recursion(num, p + 1, res + "*" + num[p], target, ans)

        ans = []
        recursion(num, 1, num[0], target, ans)
        return ans