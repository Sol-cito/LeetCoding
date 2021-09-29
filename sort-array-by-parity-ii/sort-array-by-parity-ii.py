class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans, even, odd = [0] * len(nums), 0, 1
        for ele in nums:
            if ele % 2 == 0:
                ans[even] = ele
                even +=2
            else:
                ans[odd] = ele
                odd +=2
        return ans
        