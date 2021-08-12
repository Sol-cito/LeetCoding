class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        arr = sorted(list(map(lambda x: ("".join(sorted(list(x))), x), strs)))
        res, comp = [], ""
        for ele in arr:
            if len(res) == 0 or comp == ele[0]:
                res.append(ele[1])
            else:
                ans.append(res)
                res = [ele[1]]
            comp = ele[0]
        if len(res) > 0: ans.append(res)
        return ans