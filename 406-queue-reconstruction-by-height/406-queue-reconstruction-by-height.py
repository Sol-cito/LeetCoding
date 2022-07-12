class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        ans = [None for _ in range(len(people))]
        for h, k in people:
            p, cnt = 0, 0
            while cnt < k or ans[p]:
                if not ans[p] or ans[p][0] == h: cnt += 1
                p += 1
            ans[p] = [h, k]
        return ans