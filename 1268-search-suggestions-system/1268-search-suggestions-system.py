class Node:
    def __init__(self, letter):
        self.letter = letter
        self.dic = {}
        self.set = set([])
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def makeTrie(cur, word, idx):
            if idx == len(word): return
            if word[idx] not in cur.dic:
                n = Node(word[idx])
                n.set.add(word)
                cur.dic[word[idx]] = n
                makeTrie(n, word, idx + 1)
            else:
                cur.dic.get(word[idx]).set.add(word)
                makeTrie(cur.dic.get(word[idx]), word, idx + 1)

        def search(cur, searchWord, idx, ans):
            if idx == len(searchWord):return
            for l in cur.dic.keys():
                if searchWord[idx] == l:
                    ans[idx] = sorted(list(cur.dic.get(l).set))[:3]
                    search(cur.dic.get(l), searchWord, idx + 1, ans)

        root = Node("")
        for word in products:
            makeTrie(root, word, 0)
        ans = [[] for _ in range(len(searchWord))]
        search(root, searchWord, 0, ans)
        return ans