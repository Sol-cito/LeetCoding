class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False
        nums.sort()
        dic = {}
        keys = []
        for n in nums:
            if n not in dic:
                dic[n] = 0
                keys.append(n)
            dic[n] += 1
        keyIdx, cnt = 0, 0
        while keyIdx < len(keys):
            nextKeyIdx = keyIdx
            for n in range(keys[keyIdx], keys[keyIdx] + k):
                if n not in dic or dic.get(n) == 0: return False
                dic[n] -= 1
                if dic.get(n) == 0: nextKeyIdx += 1
            keyIdx = nextKeyIdx
        return True