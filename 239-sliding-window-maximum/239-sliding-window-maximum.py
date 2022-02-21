class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def binSearch(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid =  (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        sw = sorted(nums[:k])
        ans = [sw[-1]]
        for i in range(len(nums) - k):
            del sw[binSearch(sw, nums[i])]
            sw.insert(binSearch(sw, nums[i + k]), nums[i + k])
            ans.append(sw[-1])   
        return ans