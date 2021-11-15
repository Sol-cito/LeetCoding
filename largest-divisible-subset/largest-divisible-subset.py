class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [set([])] * len(nums)
        nums.sort()
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j].copy()
                    dp[i].add(nums[i])
                    if len(dp[i]) > len(ans): ans = dp[i]
        return ans