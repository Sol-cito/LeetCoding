class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for e in s:
            if not stack or stack[-1][0] != e:
                stack.append([e, 1])
            else:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
        ans = ""
        for e in stack:
            ans += e[0] * e[1]
        return ans