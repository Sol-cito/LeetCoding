class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        total = 0
        ans = 0
        for ele in nums:
            total += ele
            if total == k: ans += 1
            if total - k in dic:
                ans += dic.get(total - k)
            if total in dic:
                dic[total] = dic.get(total) + 1
            else:
                dic[total] = 1
        return ans