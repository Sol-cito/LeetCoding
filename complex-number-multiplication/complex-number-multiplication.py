class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = num1.split('+'), num2.split('+')
        num = int(a[0]) * int(b[0]) - (int(a[1][:len(a[1]) - 1]) * int(b[1][:len(b[1]) - 1]))
        cp = str(int(a[0]) * int(b[1][:len(b[1]) - 1]) + int(a[1][:len(a[1]) - 1]) * int(b[0])) + 'i'
        return str(num) + '+' + cp