class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sum = 0
        for i in reversed(range(len(shifts))):
            val = shifts[i]
            shifts[i] += sum
            sum += val
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        ans = ''
        for i in range(len(s)):
            ans += alpha[(ord(s[i]) - 97 + shifts[i]) % 26]
        return ans