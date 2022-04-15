class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr, r = [], 1
        while r <= n:
            if n % r == 0:
                arr.append(r)
            r +=1
        if len(arr) <= k - 1:return -1
        return arr[k - 1]