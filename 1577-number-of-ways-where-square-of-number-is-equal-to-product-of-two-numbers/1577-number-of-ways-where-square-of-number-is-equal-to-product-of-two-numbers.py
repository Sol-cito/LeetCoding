class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def makeDic(target):
            dic = {}
            for i in range(len(target) - 1):
                for j in range(i + 1, len(target)):
                    p = target[i] * target[j]
                    if p in dic.keys():
                        dic[p] = dic.get(p) + 1
                    else:
                        dic[p] = 1
            return dic
        
        def countRes(numArr, dic):
            res = 0
            for e in numArr:
                if e ** 2 in dic.keys():
                   res += dic.get(e ** 2)
            return res
        
        ans = 0
        num1Dic, num2Dic = makeDic(nums1), makeDic(nums2)
        return countRes(nums1, num2Dic) + countRes(nums2, num1Dic)