class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        heap = []
        for i in range(len(values)):
            heapq.heappush(heap, [-values[i] + i, i])
        ans = 0
        for i in range(len(values)):
            while heap:
                pop = heapq.heappop(heap)
                if pop[1] <= i: continue
                ans = max(ans, values[i] - (pop[0] - i))
                heapq.heappush(heap, [pop[0], pop[1]])
                break
        return ans