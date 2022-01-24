class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        numOfUpper = len(list(filter(lambda x: ord(x) <= 90, word)))
        return numOfUpper == len(word) or (numOfUpper == 1 and ord(word[0]) <= 90) or numOfUpper == 0