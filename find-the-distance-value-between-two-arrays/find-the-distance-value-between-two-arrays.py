class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for ele in arr1:
            flag = True
            for e in arr2:
                if abs(e - ele) <= d:flag = False
            if flag:ans +=1
        return ans
        