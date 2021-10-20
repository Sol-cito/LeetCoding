class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = {}
        for i in range(len(time)):
            if time[i] not in dic.keys():
                dic[time[i]] = [i]
            else:
                dic.get(time[i]).append(i)
        ans = 0
        for i in range(len(time)):
            r = 60 - time[i] % 60
            while r <= 540:
                cnt = 0
                if r in dic.keys():
                    for ele in dic.get(r):
                        if ele > i: cnt += 1
                ans += cnt
                r += 60
        return ans