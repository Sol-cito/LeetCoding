class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        ans = 0
        S = set([])
        for i in range(len(grid) - 1):
            cnt = 0
            for j in range(len(grid)):
                if j in S: continue
                if sum(grid[j][i + 1:]) == 0:
                    ans += cnt
                    S.add(j)
                    break
                cnt += 1
        return ans if len(S) == len(grid) - 1 else -1