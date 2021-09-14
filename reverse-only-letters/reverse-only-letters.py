class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        p1, p2 = 0, len(s) - 1
        arr = list(s)
        while p1 < p2:
            while p1 < p2 and (122 < ord(arr[p1]) or 90 < ord(arr[p1]) < 97 or ord(arr[p1]) < 65):
                p1 += 1
            while p1 < p2 and (122 < ord(arr[p2]) or 90 < ord(arr[p2]) < 97 or ord(arr[p2]) < 65):
                p2 -= 1
            dummy = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = dummy
            p1 += 1
            p2 -= 1
        return "".join(arr)