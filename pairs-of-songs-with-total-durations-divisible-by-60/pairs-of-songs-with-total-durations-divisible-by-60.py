class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = {}
        for t in time:
            if t not in dic.keys():
                dic[t] = 1
            else:
                dic[t] = dic.get(t) + 1
        ans = 0
        for key in dic.keys():
            if (key * 2) % 60 == 0: ans += (dic.get(key) * (dic.get(key) - 1)) // 2
            r = 60 - key % 60
            while r <= 500:
                if r in dic.keys() and r > key: ans += dic.get(key) * dic.get(r)
                r += 60
        return ans
