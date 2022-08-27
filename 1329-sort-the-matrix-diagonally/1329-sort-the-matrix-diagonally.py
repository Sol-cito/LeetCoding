class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def recursion(x, y, heap):
            if x >= len(mat) or y >= len(mat[0]):return
            heapq.heappush(heap, -mat[x][y])
            recursion(x + 1, y + 1, heap)
            mat[x][y] = -heapq.heappop(heap)
        
        
        for i in range(len(mat)):
            recursion(i, 0, [])
        for i in range(len(mat[0])):
            recursion(0, i, [])
        return mat
            