class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def search(arr, idx, res, check, ans):
            for i in range(idx, len(arr)):
                if not check[i]: continue
                flag = True
                for l in arr[i]:
                    if l in res:
                        flag = False
                        break
                if flag:
                    ans = max(ans, search(arr, i + 1, res + arr[i], check, len(res + arr[i])))
            return ans

        check = [True] * len(arr)
        for i in range(len(arr)):
            c = [0] * 26
            for l in arr[i]:
                c[ord(l) - 97] += 1
                if c[ord(l) - 97] > 1:
                    check[i] = False
        return search(arr, 0, "", check, 0)