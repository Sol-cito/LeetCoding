class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        que = []
        for x, y in points:
            heapq.heappush(que, (x**2 + y**2, [x, y]))
        cnt = 0
        ans = []
        while cnt < k:
            ans.append(heapq.heappop(que)[1])
            cnt +=1
        return ans
        
            