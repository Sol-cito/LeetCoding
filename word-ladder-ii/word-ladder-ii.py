class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        def comp(w1, w2):
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]: cnt += 1
            return cnt == 1

        if endWord not in wordList: return []
        if beginWord not in wordList:wordList.append(beginWord)
        dic = dict(zip(wordList, [len(wordList) for _ in range(len(wordList))]))
        dic[endWord] = 1
        que = deque([[endWord, 1, endWord]])
        ans = []
        while que:
            pop = que.pop()
            if pop[0] == beginWord: ans.append(pop[2].split(","))
            for word in wordList:
                if pop[1] <= dic.get(word) and comp(pop[0], word):
                    dic[word] = pop[1]
                    que.appendleft([word, pop[1] + 1, word + "," + pop[2]])
        return ans