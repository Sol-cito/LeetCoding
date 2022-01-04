class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x, y = "0b", bin(n)
        for i in range(2, len(y)):
            x += str(1 - int(y[i]))
        return int(x, 2)