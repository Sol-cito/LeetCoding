class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inBound = [0] * numCourses
        dic = dict(zip([i for i in range(numCourses)], [[] for _ in range(numCourses)]))
        for a, b in prerequisites:
            inBound[a] += 1
            dic.get(b).append(a)
        que = deque([])
        for i in range(len(inBound)):
            if inBound[i] == 0: que.appendleft(i)
        ans = []
        while que:
            pop = que.pop()
            ans.append(pop)
            for linked in dic.get(pop):
                inBound[linked] -= 1
                if inBound[linked] == 0: que.appendleft(linked)
        if len(ans) != numCourses:return []
        return ans
