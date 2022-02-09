class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic.get(nums[i]).append(i)
        ans = 0
        S = set([])
        for i in range(len(nums)):
            if nums[i] in S: continue
            a, b = nums[i] - k, nums[i] + k
            if a in dic.keys() and dic.get(a)[-1] > i and a not in S:
                ans += 1
                S.add(nums[i])
            if a == b: continue
            if b in dic.keys() and dic.get(b)[-1] > i and b not in S:
                ans += 1
                S.add(nums[i])
        return ans