class WordFilter:
    def __init__(self, words: List[str]):
        self.words = words
        self.preTrie = {}
        self.suffTrie = {}
        for i in range(len(words)):
            self.makeTrie(words[i], i, self.preTrie, 0)
            self.makeTrie(words[i][::-1], i, self.suffTrie, 0)

    def makeTrie(self, word, wordIdx, dic, idx):
        if idx == len(word) - 1:
            dic[word[idx]] = [{}, set([wordIdx])]
            return
        if word[idx] not in dic.keys():
            dic[word[idx]] = [{}, set([wordIdx])]
        else:
            dic.get(word[idx])[1].add(wordIdx)
        self.makeTrie(word, wordIdx, dic.get(word[idx])[0], idx + 1)

    def f(self, prefix: str, suffix: str) -> int:
        r1 = self.search(self.preTrie, prefix, 0)
        r2 = self.search(self.suffTrie, suffix[::-1], 0)
        if r1 != -1 and r2 != -1:
            res = 0
            for e in r1:
                if e in r2: res = max(res, e)
            return res
        return -1

    def search(self, dic, word, idx):
        if idx == len(word) - 1:
            if word[idx] not in dic.keys(): return -1
            return dic.get(word[idx])[1]

        if word[idx] not in dic: return -1
        return self.search(dic.get(word[idx])[0], word, idx + 1)