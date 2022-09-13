class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        que = deque([])
        totalNum = 0
        arr = [0] * len(nums)
        heap = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                heapq.heappush(heap, [nums[i][j], i])
        minRange = 10 ** 10
        ans = []
        while heap:
            num, arrIdx = heapq.heappop(heap)
            que.appendleft([num, arrIdx])
            arr[arrIdx] += 1
            if arr[arrIdx] == 1:
                totalNum += 1
            if totalNum == len(nums):
                while totalNum == len(nums):
                    if que[0][0] - que[-1][0] < minRange:
                        minRange = que[0][0] - que[-1][0]
                        ans = [que[-1][0], que[0][0]]
                    pop = que.pop()
                    arr[pop[1]] -= 1
                    if arr[pop[1]] == 0:
                        totalNum -= 1
        return ans