class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        arr = [0] * 201
        for ele in nums:
            arr[ele + 100] +=1
        que = []
        for ele in nums:
            heapq.heappush(que, (arr[ele + 100], -ele))
        ans = []
        while que:
            pop = heapq.heappop(que)
            ans.append(-pop[1])
        return ans