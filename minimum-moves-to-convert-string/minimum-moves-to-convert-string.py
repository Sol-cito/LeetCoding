class Solution:
    def minimumMoves(self, s: str) -> int:
        pointer, ans = 0, 0
        while pointer < len(s):
            if s[pointer] == 'X':
                pointer +=2
                ans +=1
            pointer +=1
        return ans