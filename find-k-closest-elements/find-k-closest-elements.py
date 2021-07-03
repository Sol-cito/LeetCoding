import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap = []
        for ele in arr:
            heapq.heappush(heap, (abs(ele - x), ele))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        ans.sort()
        return ans