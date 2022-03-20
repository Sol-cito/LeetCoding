class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def helper(l1, l2):
            a = len(l1) + 1
            for num in range(1, 7):
                res = 0
                for i in range(len(l1)):
                    if l1[i] != num and l2[i] != num:
                        res = len(l1) + 1
                        break
                    if l1[i] != num and l2[i] == num:
                        res +=1
                a = min(a, res)
            if a == len(l1) + 1:return -1
            return a
        
        a1, a2 = helper(tops, bottoms), helper(bottoms, tops)
        if a1 == a2 == -1:return -1
        return min(a1, a2)
                