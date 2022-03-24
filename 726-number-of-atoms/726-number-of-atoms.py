class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def recursion(idx, word):
            dic1, atom, cnt = {}, "", 1
            while idx < len(word):
                if 65 <= ord(word[idx]) <= 90:
                    if len(atom) > 0:
                        dic1[atom] = dic1.get(atom) + int(cnt) if atom in dic1.keys() else int(cnt)
                        cnt = 1
                    atom = word[idx]
                elif 97 <= ord(word[idx]) <= 122:
                    atom += word[idx]
                elif word[idx] == '(':
                    res = recursion(idx + 1, word)
                    mergeDics(dic1, res[0])
                    idx = res[1]
                elif 48 <= ord(word[idx]) <= 57:
                    if cnt == 1: cnt = ""
                    cnt += word[idx]
                else:
                    if len(atom) > 0:
                        dic1[atom] = dic1.get(atom) + int(cnt) if atom in dic1.keys() else int(cnt)
                    idx += 1
                    num = ""
                    while idx < len(word) and 48 <= ord(word[idx]) <= 57:
                        num += word[idx]
                        idx += 1
                    if len(num) > 0: multiplyDic(dic1, int(num))
                    return [dic1, idx - 1]
                idx += 1
            if len(atom) > 0:
                dic1[atom] = dic1.get(atom) + int(cnt) if atom in dic1.keys() else int(cnt)
            return [dic1, idx]

        def mergeDics(dic1, dic2):
            for k in dic2.keys():
                if k in dic1.keys():
                    dic1[k] = dic1.get(k) + dic2.get(k)
                else:
                    dic1[k] = dic2.get(k)
            return dic1

        def multiplyDic(dic, num):
            for k in dic.keys():
                dic[k] = dic.get(k) * num

        dic = recursion(0, formula)[0]
        atomArr = []
        ans = ""
        for k in dic.keys():
            atomArr.append(k)
        for k in sorted(atomArr):
            if dic.get(k) == 1:
                ans += k
            else:
                ans += k + str(dic.get(k))
        return ans