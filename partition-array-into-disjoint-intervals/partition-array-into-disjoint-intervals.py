class Solution:
    def partitionDisjoint(self, nums) -> int:
        n = nums[-1]
        arr = [10 ** 6] * len(nums)
        for i in reversed(range(len(nums) - 1)):
            arr[i] = min(n, arr[i])
            n = min(n, nums[i])
        maxVal = nums[0]
        ans = 0
        for i in range(len(nums)):
            if maxVal <= arr[i]:
                ans = i + 1
                break
            maxVal = max(maxVal, nums[i])
        return ans