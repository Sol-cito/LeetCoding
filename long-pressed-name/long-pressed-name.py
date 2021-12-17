class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(name) and p2 < len(typed):
            pre1, cnt1 = name[p1], 0
            while p1 < len(name) and name[p1] == pre1:
                cnt1 +=1
                p1 +=1
            pre2, cnt2 = typed[p2], 0
            while p2 < len(typed) and typed[p2] == pre2:
                cnt2 +=1
                p2 +=1
            if pre1 != pre2 or cnt1 > cnt2:return False
        return p1 == len(name) and p2 == len(typed)
            
                