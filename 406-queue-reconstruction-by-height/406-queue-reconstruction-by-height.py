class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        ans = [None for _ in range(len(people))]
        for i in range(len(people)):
            h, k = people[i][0], people[i][1]
            p, cnt = 0, 0
            while cnt < k or ans[p]:
                if not ans[p] or ans[p][0] == h: cnt += 1
                p += 1
            ans[p] = people[i]
        return ans