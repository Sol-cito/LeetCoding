class Solution:
    def findComplement(self, num: int) -> int:
        x, y = "0b", bin(num)
        for i in range(2, len(y)):
            x += str(1 - int(y[i]))
        return int(x, 2)