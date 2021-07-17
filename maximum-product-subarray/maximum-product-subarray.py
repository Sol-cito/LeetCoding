class Solution:
    def maxProduct(self, nums) -> int:
        ans = nums[0]
        res, firstWindow, idx = 1, 1, -1
        for i in range(len(nums)):
            if nums[i] == 0:
                res, firstWindow, idx = 1, 1, -1
                ans = max(ans, 0)
                continue
            if nums[i] > 0:
                res *= nums[i]
                if idx == -1: firstWindow *= nums[i]
            elif nums[i] < 0:
                res *= nums[i]
                if idx == -1:
                    firstWindow *= nums[i]
                    idx = i
            if idx == i:
                ans = max(ans, res)
            else:
                ans = max(ans, res, res // firstWindow)
        return ans