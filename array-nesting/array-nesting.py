class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visit = [False] * len(nums)
        ans = 0
        for i in range(len(nums)):
            if visit[i]: continue
            p, cnt = i, 0
            while not visit[p]:
                visit[p] = True
                p = nums[p]
                cnt += 1
            ans = max(ans, cnt)
        return ans