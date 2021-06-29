class Solution(object):
    def longestOnes(self, nums, k):
        arr = []
        for n in nums:
            if n == 0:
                arr.append(n)
            else:
                if not arr or arr[-1] == 0:
                    arr.append(n)
                else:
                    arr[-1] += 1
        if k == 0: return max(arr)
        dic, idx = {}, 0
        for i in range(len(arr)):
            left, right = 0, 0
            if i != 0: left = arr[i - 1]
            if i != len(arr) - 1: right = arr[i + 1]
            if arr[i] == 0:
                dic[idx] = (left, right)
                idx += 1
        ans = 0
        right = min(len(dic) - 1, k - 1)
        for i in range(min(len(dic), k)):
            ans += 1 + dic.get(i)[1]
            if i == 0 or dic.get(i - 1)[1] == 0: ans += dic.get(i)[0]
        res = ans
        for i in range(len(dic) - right - 1):
            res -= dic.get(i)[0]
            res += dic.get(right + 1)[1]
            right += 1
            ans = max(ans, res)
        return ans