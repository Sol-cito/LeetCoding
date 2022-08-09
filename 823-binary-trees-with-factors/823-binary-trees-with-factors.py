class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dic = {e: 1 for e in arr}
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in dic:
                    dic[arr[i]] = dic.get(arr[i]) + dic.get(arr[i] // arr[j]) * dic.get(arr[j])
        return sum(list(map(lambda x: dic.get(x), dic.keys()))) % (10 ** 9 + 7)