class TrieNode:
    def __init__(self, letter: str, isEnd: bool):
        self.letter = letter
        self.isEnd = isEnd
        self.link = {}

class StreamChecker:
    def __init__(self, words: List[str]):
        self.words = words
        self.root = TrieNode('', False)
        self.target = ""
        for w in self.words:
            self.makeTrie(self.root, w, len(w) - 1)

    def makeTrie(self, cur, word, idx):
        if idx == -1:
            cur.isEnd = True
            return
        if word[idx] not in cur.link.keys():
            cur.link[word[idx]] = TrieNode(word[idx], False)
            self.makeTrie(cur.link.get(word[idx]), word, idx - 1)
        else:
            self.makeTrie(cur.link.get(word[idx]), word, idx - 1)

    def query(self, letter: str) -> bool:
        self.target += letter
        return self.isIncluded(self.root, self.target, len(self.target) - 1)

    def isIncluded(self, cur, target, idx):
        if cur.isEnd: return True
        if idx == -1: return cur.isEnd
        if target[idx] in cur.link.keys():
            return self.isIncluded(cur.link.get(target[idx]), target, idx - 1)
        return False