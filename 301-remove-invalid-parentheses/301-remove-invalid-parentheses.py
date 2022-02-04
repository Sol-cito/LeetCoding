class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def recursion(p, s, left, right, cur, ans):
            if p == len(s) and left == right == 0:
                ans.add(cur)
                return
            for i in range(p, len(s)):
                if s[i] not in ['(', ')']:
                    return recursion(i + 1, s, left, right, cur + s[i], ans)
                elif s[i] == '(' and left > 0:
                    recursion(i + 1, s, left - 1, right, cur + s[i], ans)
                elif s[i] == ')' and left < right:
                    recursion(i + 1, s, left, right - 1, cur + s[i], ans)
                elif left == right == 0:
                    recursion(i + 1, s, left, right, cur, ans)
        
        
        stack = []
        validNum = 0
        for l in s:
            if l == '(':
                stack.append(1)
            elif l == ')':
                if not stack:continue
                stack.pop()
                validNum +=1
        ans = set([])
        recursion(0, s, validNum, validNum, "", ans)
        return ans
        