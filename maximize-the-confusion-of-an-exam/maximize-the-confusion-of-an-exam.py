class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def twoPointer(answerKey, target, k):
            res, p1, p2 = 0, 0, 0
            while p1 < len(answerKey):
                if answerKey[p1] != target:
                    p1 += 1
                else:
                    if k > 0:
                        k -= 1
                        p1 += 1
                    else:
                        while p2 < p1:
                            if answerKey[p2] == target:
                                k += 1
                                p2 += 1
                                break
                            p2 += 1
                res = max(res, p1 - p2)
            return res

        return max(twoPointer(answerKey, 'F', k), twoPointer(answerKey, 'T', k))