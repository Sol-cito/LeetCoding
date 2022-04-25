class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = [0] * n
        for a, b in edges:
            arr[b] +=1
        ans = []
        for i in range(len(arr)):
            if arr[i] == 0:
                ans.append(i)
        return ans