class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        def binSearch(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        arr = nums1.copy()
        ans = res = 0
        arr.sort()
        for i in range(len(nums2)):
            ans += abs(nums1[i] - nums2[i])
            r = binSearch(arr, nums2[i])
            if r < len(arr):
                res = max(res, abs(nums1[i] - nums2[i]) - abs(arr[r] - nums2[i]))
            if r > 0:
                res = max(res, abs(nums1[i] - nums2[i]) - abs(arr[r - 1] - nums2[i]))
        return (ans - res) % (10 ** 9 + 7)