class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        def binSearch(dp, target):
            l, r = 0, len(dp)
            while l <= r:
                mid = (l + r) // 2
                if dp[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            dp[l] = target

        dp = [nums[0]]
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                if len(dp) >= 3: return True
            else:
                binSearch(dp, nums[i])
        return False