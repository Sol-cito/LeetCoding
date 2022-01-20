class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 10 ** 13
        while l <= r:
            mid = (l + r) // 2
            res = 0
            for ele in piles:
                res += math.ceil(ele / mid)
            if res <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l