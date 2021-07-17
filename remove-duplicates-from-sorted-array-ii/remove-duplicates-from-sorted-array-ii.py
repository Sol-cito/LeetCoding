class Solution:
    def removeDuplicates(self, nums) -> int:
        p1, p2, cnt = 0, 1, 1
        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                if cnt == 1:
                    p1 += 1
                    nums[p1] = nums[p2]
                    cnt = 2
                p2 += 1
            else:
                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1
                cnt = 1
        return p1 + 1