class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        dic = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dic or len(dic.get(groupSizes[i])) == 0:
                dic[groupSizes[i]] = [i]
            else:
                dic.get(groupSizes[i]).append(i)
            if len(dic.get(groupSizes[i])) == groupSizes[i]:
                ans.append(dic.get(groupSizes[i]))
                dic[groupSizes[i]] = []
        return ans