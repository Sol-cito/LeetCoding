class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def binSearch(target, arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
            
        ans = 0
        arr = [nums[-1] * 2]
        for i in range(len(nums) - 2, -1, -1):
            ans += binSearch(nums[i], arr)
            arr.insert(binSearch(nums[i] * 2, arr), nums[i] * 2)
        return ans
            