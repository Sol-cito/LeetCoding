class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def helper(input, target):
            alpha = [0] * 26
            for e in input:
                alpha[ord(e) - 97] += 1
            for l in target:
                isFound = False
                for i in range(ord(l) - 97, len(alpha)):
                    if alpha[i] > 0:
                        alpha[i] -= 1
                        isFound = True
                        break
                if not isFound: return False
            return True

        return helper(s1, s2) or helper(s2, s1)