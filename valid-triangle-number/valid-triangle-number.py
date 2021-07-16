class Solution:
    def binSearch(self, nums, n1, n2, idx):
        l, r = idx, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < n1 + n2:
                l = mid + 1
            else:
                r = mid - 1
        return r

    def triangleNumber(self, nums):
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                ans += self.binSearch(nums, nums[i], nums[j], j + 1) - j
        return ans

        