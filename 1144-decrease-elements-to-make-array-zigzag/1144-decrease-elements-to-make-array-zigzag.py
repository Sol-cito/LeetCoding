class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def helper(start):
            res = 0
            for i in range(start, len(nums), 2):
                a = nums[i] - nums[i - 1] + 1 if i > 0 else 0
                b = nums[i] - nums[i + 1] + 1 if i < len(nums) - 1 else 0
                res += max(0, a, b)
            return res

        return min(helper(0), helper(1))