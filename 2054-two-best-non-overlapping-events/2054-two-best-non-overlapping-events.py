class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        def binSearch(arr, target):
            if arr[-1][0] < target: return 0
            l, r = 0, len(arr)
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return arr[l][1]

        events.sort()
        arr = deque([])
        ans = 0
        maxVal = 0
        for s, e, v in reversed(events):
            maxVal = max(maxVal, v)
            arr.appendleft([s, maxVal])
        for s, e, v in events:
            r = binSearch(arr, e + 1)
            ans = max(ans, v + r)
        return ans