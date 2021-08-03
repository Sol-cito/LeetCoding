class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def recursion(startIdx, nums, res, S, ans):
            r = "".join(map(lambda x:chr(x + 107), res))
            if r not in S:
                ans.append(res.copy())
                S.add(r)
            if startIdx == len(nums):
                return
            for i in range(startIdx, len(nums)):
                res.append(nums[i])
                recursion(i + 1, nums, res, S, ans)
                del res[-1]
                  
        ans = []
        S = set([])
        nums.sort()
        recursion(0, nums, [], S, ans)
        return ans
        