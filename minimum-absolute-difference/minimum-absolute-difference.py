class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        dic = {}
        smallest = arr[-1]
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            smallest = min(smallest, diff)
            if diff in dic.keys():
                dic.get(diff).append([arr[i - 1], arr[i]])
            else:
                dic[diff] = [[arr[i - 1], arr[i]]]
        return dic.get(smallest)