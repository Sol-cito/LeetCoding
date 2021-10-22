class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        dic = {}
        for l in s:
            if l in dic:
                dic[l] = dic.get(l) + 1
            else:
                dic[l] = 1
        for l in s:
            heapq.heappush(heap, (-dic.get(l), l))
        ans = ''
        while heap:
            ans += heapq.heappop(heap)[1]
        return ans