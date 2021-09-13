class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        alpha = [0] * 26
        for l in text: alpha[ord(l) - 97] += 1
        return min(alpha[0], alpha[1], alpha[11]//2, alpha[14]//2, alpha[13])
