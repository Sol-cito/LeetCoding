class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, res, ans = 0, 1, nums[0], len(nums) + 1
        while l < r:
            if res >= target:
                ans = min(ans, r - l)
                res -= nums[l]
                l +=1
            elif res < target and r < len(nums):
                res += nums[r]
                r +=1
            else:
                res -= nums[l]
                l +=1
        return ans if ans < len(nums) + 1 else 0
                
                