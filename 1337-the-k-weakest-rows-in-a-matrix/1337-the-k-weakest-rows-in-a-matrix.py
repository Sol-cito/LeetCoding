class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap, ans = [], []
        for i in range(len(mat)):
            heapq.heappush(heap, [sum(mat[i]), i])
        cnt = 0
        while cnt < k:
            ans.append(heapq.heappop(heap)[1])
            cnt += 1
        return ans