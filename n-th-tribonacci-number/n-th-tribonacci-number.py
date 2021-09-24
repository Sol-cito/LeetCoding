class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:return 0
        arr, sum, p = [0, 1, 1], 2, 0
        for i in range(2, n):
            arr.append(sum)
            sum += arr[-1]
            sum -= arr[p]
            p +=1
        return arr[-1]