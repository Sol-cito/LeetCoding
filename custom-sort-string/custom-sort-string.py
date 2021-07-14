class Solution:
    def customSortString(self, order: str, str: str) -> str:
        rest = ""
        dic, arr = {}, [""] * 26
        for i in range(len(order)):
            dic[order[i]] = ord(order[i]) - 97
        for l in str:
            if l not in dic.keys():
                rest += l
            else:
                arr[ord(l) - 97] += l
        ans = ""
        for o in order:
            ans += arr[dic.get(o)]
        return ans + rest