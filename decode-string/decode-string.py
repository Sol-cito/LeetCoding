class Solution:
    def decodeString(self, s: str) -> str:
        def decode(target, start, num):
            res = ""
            p = start
            while p < len(target):
                if target[p] == ']':
                    start = p
                    break
                if 97 <= ord(target[p]) <= 122:
                    res += target[p]
                else:
                    nextNum = ""
                    while 48 <= ord(target[p]) <= 57:
                        nextNum += target[p]
                        p += 1
                    r = decode(target, p + 1, int(nextNum))
                    res += r[0]
                    p = r[1]
                p += 1
            return [num * res, start]

        return decode(s, 0, 1)[0]