class MedianFinder(object):
    arr = []

    def binSearch(self, target):
        l, r = 0, len(self.arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.arr[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def __init__(self):
        self.arr = []

    def addNum(self, num):
        idx = self.binSearch(num)
        self.arr.insert(idx, num)

    def findMedian(self):
        l = len(self.arr)
        if len(self.arr) % 2 == 0:
            return (self.arr[l // 2] + self.arr[l // 2 - 1]) / 2
        else:
            return self.arr[l // 2]