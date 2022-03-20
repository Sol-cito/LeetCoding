class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res1 = res2 = len(tops) + 1
        for num in range(1, 7):
            cnt1, cnt2 = 0, 0
            for i in range(len(tops)):
                if cnt1 == cnt2 == len(tops) + 1:break
                if tops[i] != num and bottoms[i] == num and cnt1 != len(tops) + 1:
                    cnt1 +=1
                elif tops[i] != num and bottoms[i] != num:
                    cnt1 = len(tops) + 1
                if bottoms[i] != num and tops[i] == num and cnt2 != len(tops) + 1:
                    cnt2 +=1
                elif bottoms[i] != num and tops[i] != num:
                    cnt2 = len(tops) + 1
            res1, res2 = min(res1, cnt1), min(res2, cnt2)
        if res1 == res2 == len(tops) + 1:return -1
        return min(res1, res2)
