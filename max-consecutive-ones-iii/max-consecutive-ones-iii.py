class Solution(object):
    def longestOnes(self, nums, k):
        left, right, res, ans, zeroCnt = 0, 0, 0, 0, 0
        while right < len(nums):
            if zeroCnt < k or nums[right] == 1:
                res += 1
                zeroCnt += nums[right] == 0
                right += 1
            else:
                res -= 1
                zeroCnt -= nums[left] == 0
                left += 1
            ans = max(ans, res)
        return ans