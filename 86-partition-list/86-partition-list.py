class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sCur, firstS = None, None
        geCur, firstGe = None, None
        cur = head
        while cur:
            if cur.val < x:
                if not firstS:
                    firstS = cur
                    sCur = firstS
                elif sCur:
                    sCur.next = cur
                    sCur = cur
            else:
                if not firstGe:
                    firstGe = cur
                    geCur = firstGe
                elif geCur:
                    geCur.next = cur
                    geCur = cur
            cur = cur.next
        if geCur:geCur.next = None
        if sCur:sCur.next = firstGe
        return firstS if firstS else firstGe
            