class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1: return ""
        aFlag = True
        target = len(palindrome)
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                aFlag = False
                target = min(target, i)
        if aFlag: return palindrome[:len(palindrome) - 1] + 'b'
        return palindrome[:target] + 'a' + palindrome[target + 1:]