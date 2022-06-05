class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return 1
        nums.sort()
        ans = 1
        p1, p2, total = 0, 1, nums[0]
        while p1 < len(nums):
            while p2 < len(nums) and (p2 - p1) * nums[p2] <= total + k:
                total += nums[p2]
                p2 += 1
            ans = max(ans, p2 - p1)
            total -= nums[p1]
            p1 += 1
        return ans