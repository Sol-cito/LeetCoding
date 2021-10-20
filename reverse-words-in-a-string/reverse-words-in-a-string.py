class Solution:
    def reverseWords(self, s: str) -> str:
        stack = s.split(" ")
        ans = ""
        while stack:
            pop = stack.pop()
            if pop == "":continue
            ans += pop+" "
        return ans.strip()