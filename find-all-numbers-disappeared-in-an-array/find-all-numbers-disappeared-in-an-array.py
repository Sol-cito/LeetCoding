class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        exist = [False] * len(nums)
        for ele in nums:
            exist[ele - 1] = True
        ans = []
        for i in range(len(exist)):
            if not exist[i]:ans.append(i + 1)
        return ans