class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        idx = 0
        for i in range(len(binary)):
            if binary[i] == "0":
                idx = i
                break
        zero, one = 0, 0
        ans = "1" * idx
        for i in range(idx, len(binary)):
            if binary[i] == "0":
                zero += 1
            else:
                one += 1
        ans += "1" * (zero - 1)
        if zero > 0:
            ans += "0"
        ans += ("1" * one)
        return ans