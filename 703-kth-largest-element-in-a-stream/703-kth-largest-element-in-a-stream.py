class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def binSearch(self, target):
        l, r = 0, len(self.nums) - 1
        mid = (l + r) // 2
        while l <= r:
            if self.nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2
        return l
        
    def add(self, val: int) -> int:
        self.nums.insert(self.binSearch(val), val)
        return self.nums[len(self.nums) - self.k]

