class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def binSearch(l, arr, target):
            r = len(arr) - 1
            mid = (l + r) // 2
            while l <= r:
                if arr[mid] < target:
                    r = mid - 1
                else:
                    l = mid + 1
                mid = (l + r) // 2
            return r

        ans = 0
        for i in range(len(nums1)):
            res = binSearch(i, nums2, nums1[i])
            ans = max(ans, res - i)
        return ans