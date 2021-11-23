class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = []
        for i in range(len(s)):
            diff = abs(ord(s[i]) - ord(t[i]))
            arr.append(diff)
        ans = 0
        p2 = 0
        for p1 in range(len(arr)):
            while p2 < len(arr) and maxCost >= arr[p2]:
                maxCost -= arr[p2]
                p2 += 1
            maxCost += arr[p1]
            ans = max(ans, p2 - p1)
        return ans