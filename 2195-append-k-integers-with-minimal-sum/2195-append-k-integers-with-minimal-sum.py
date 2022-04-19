class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        p, ans = 0, 0
        for e in nums:
            if p == e:continue
            s = (e - p - 1) * (p + 1 + e - 1) // 2
            if k >= e - p - 1:
                k -= (e - p - 1)
                ans += s
            else:
                break
            p = e
        ans += k * (p + 1 + p + k) // 2
        return ans