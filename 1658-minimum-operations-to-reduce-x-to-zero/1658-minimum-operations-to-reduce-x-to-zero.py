class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        leftDic, rightDic = {}, {}
        l, r = 0, 0
        for i in range(len(nums)):
            l += nums[i]
            r += nums[len(nums) - i - 1]
            leftDic[l] = i
            rightDic[r] = len(nums) - i - 1
        ans = len(nums) + 1
        l, r = 0, 0
        for i in range(len(nums)):
            l += nums[i]
            r += nums[len(nums) - i - 1]
            if l == x:ans = min(ans, i + 1)
            if r == x:ans = min(ans, i + 1)
            if x - l in rightDic.keys() and rightDic.get(x - l) > i:
                ans = min(ans, i + 1 + len(nums) - rightDic.get(x - l))
            if x - r in leftDic.keys() and leftDic.get(x - r) < len(nums) - i - 1:
                ans = min(ans, leftDic.get(x - r) + 1 + i + 1)
        return ans if ans != len(nums) + 1 else -1
        