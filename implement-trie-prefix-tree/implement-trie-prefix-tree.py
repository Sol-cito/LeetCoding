class Trie:
    def __init__(self):
        self.S = set([])
        self.root = {}

    def insert(self, word: str) -> None:
        def makeTrie(node, word, i):
            if i == len(word): return
            if word[i] not in node.keys(): node[word[i]] = {}
            makeTrie(node.get(word[i]), word, i + 1)

        makeTrie(self.root, word, 0)
        self.S.add(word)

    def search(self, word: str) -> bool:
        return word in self.S

    def startsWith(self, prefix: str) -> bool:
        def find(node, prefix, i):
            if i == len(prefix): return True
            if prefix[i] in node.keys():
                return find(node.get(prefix[i]), prefix, i + 1)
            return False

        return find(self.root, prefix, 0)