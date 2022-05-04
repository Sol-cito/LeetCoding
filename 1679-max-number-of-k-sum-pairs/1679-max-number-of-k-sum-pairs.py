class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        for e in nums:
            if e not in dic:
                dic[e] = 1
            else:
                dic[e] = dic.get(e) + 1
        ans = 0
        for key in dic.keys():
            if k - key in dic and k - key > key:
               ans += min(dic.get(key), dic.get(k - key))
        if k % 2 == 0 and k // 2 in dic:
            ans += dic.get(k // 2) // 2
        return ans