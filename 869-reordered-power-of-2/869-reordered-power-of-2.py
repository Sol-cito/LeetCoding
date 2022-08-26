class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def recursion(arr, S, res):
            if len(res) == len(arr):
                return int(res) in S
            for i in range(len(arr)):
                if arr[i] == -1 or (len(res) == 0 and arr[i] == 0):continue
                temp = arr[i]
                arr[i] = -1
                if recursion(arr, S, res + str(temp)):return True
                arr[i] = temp
            return False
        
        
        arr = [int(l) for l in str(n)]
        S = set([1])
        two = 2
        while len(str(two)) <= len(str(n)):
            S.add(two)
            two *= 2
        return recursion(arr, S, "")
