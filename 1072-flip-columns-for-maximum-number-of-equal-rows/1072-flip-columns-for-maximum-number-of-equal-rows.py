class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        arr = []
        for row in matrix:
            res, p, cnt = "", -1, 0
            for i in range(len(row)):
                if p != row[i]:
                    if cnt != 0: res += str(cnt)
                    p = row[i]
                    cnt = 1
                else:
                    cnt += 1
            res += str(cnt)
            arr.append(res)
        ans = 1
        for i in range(len(arr)):
            res = 1
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]: res += 1
            ans = max(ans, res)
        return ans