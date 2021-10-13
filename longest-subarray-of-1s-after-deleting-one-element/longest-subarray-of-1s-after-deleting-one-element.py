class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        arr = []
        one, numOfZero = 0, 0
        for ele in nums:
            if ele == 0:
                numOfZero +=1
                if one > 0:
                    arr.append(one)
                    one = 0
                arr.append(0)
            else:
                one +=1
        if one > 0:arr.append(one)
        if numOfZero == 0:return sum(arr) - 1
        ans = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                res = 0
                if i > 0:res += arr[i - 1]
                if i < len(arr) - 1: res += arr[i + 1]
                ans = max(ans, res)
        return ans