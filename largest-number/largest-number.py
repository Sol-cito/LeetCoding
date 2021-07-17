class Solution:
    def largestNumber(self, nums) -> str:
        heap = []
        for n in nums:
            target = [str(n), n]
            for i in range(len(str(n)), 10):
                target[0] += target[0][i - len(str(n))]
            target[0] = -(int(target[0]))
            heapq.heappush(heap, target)
        ans = ""
        while heap:
            ans += str(heapq.heappop(heap)[1])
        return str(int(ans))
