class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd, even = 0, 0
        arr = deque([])
        for i in reversed(range(len(nums))):
            arr.appendleft([even, odd])
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]
        odd = even = 0
        ans = 0
        for i in range(len(nums)):
            if odd + arr[i][0] == even + arr[i][1]: ans += 1
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]
        return ans