class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        for n, u in boxTypes:
            heapq.heappush(heap, [-u, n])
        ans = 0
        while heap and truckSize > 0:
            pop = heapq.heappop(heap)
            num = min(truckSize, pop[1])
            truckSize -= num
            ans += abs(pop[0] * num)
        return ans