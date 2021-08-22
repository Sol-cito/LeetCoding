class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def getCombinations(c, startPoint, threes, basket, S):
            if len(basket) == c:
                S.add(sum(basket))
                return
            for i in range(startPoint, len(threes)):
                basket.append(threes[i])
                getCombinations(c, i + 1, threes, basket, S)
                del basket[-1]

        threes = []
        for i in range(15):
            if 3 ** i > n: break
            threes.append(3 ** i)
        S = set([])
        for i in range(1, 16):
            getCombinations(i, 0, threes, [], S)
        return n in S