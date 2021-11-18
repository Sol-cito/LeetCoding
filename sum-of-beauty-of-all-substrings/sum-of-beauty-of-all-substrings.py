class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            alpha = [0] * 26
            for j in range(i, len(s)):
                alpha[ord(s[j]) - 97] += 1
                maxVal, minVal = 0, len(s)
                for al in alpha:
                    maxVal = max(maxVal, al)
                    if al > 0: minVal = min(minVal, al)
                if maxVal > 0 and minVal < len(s): ans += maxVal - minVal
        return ans
