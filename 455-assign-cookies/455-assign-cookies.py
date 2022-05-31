class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookiePointer = 0
        ans = 0
        for e in g:
            while cookiePointer < len(s):
                if s[cookiePointer] >= e:
                    ans +=1
                    cookiePointer +=1
                    break
                cookiePointer +=1
        return ans
            