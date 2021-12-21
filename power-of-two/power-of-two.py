class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:return False
        x = math.log2(n)
        return x - math.trunc(x) == 0