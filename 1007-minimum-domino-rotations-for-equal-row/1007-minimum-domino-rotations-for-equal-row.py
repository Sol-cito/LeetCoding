class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def helper(l1, l2):
            res = len(l1) + 1
            for num in range(1, 7):
                cnt = 0
                for i in range(len(l1)):
                    if l1[i] != num and l2[i] != num:
                        cnt = len(l1) + 1
                        break
                    elif l1[i] != num and l2[i] == num:
                        cnt +=1
                res = min(res, cnt)
            return res
        
        a1, a2 = helper(tops, bottoms), helper(bottoms, tops)
        if a1 == a2 == len(tops) + 1:return -1
        return min(a1, a2)
                