class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p1, p2, p3 = 0, 0, 1
        cnt = 0
        while p2 < len(flowerbed):
            if p2 == len(flowerbed) - 1: p3 = p2
            sum = flowerbed[p1] + flowerbed[p2] + flowerbed[p3]
            if sum == 0:
                flowerbed[p2] = 1
                cnt +=1
            p1 +=1 if p2 != 0 else 0
            p2 +=1
            p3 +=1
        return cnt >= n
