class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num, S, cur = -101, set([]), head
        while cur:
            if cur.val == num:
                S.add(num)
            num = cur.val
            cur = cur.next
        prev, cur, r = None, head, None
        while cur:
            if cur.val in S:
                if prev:prev.next = None
                cur = cur.next
                continue
            if not r:r = cur
            if prev:prev.next = cur
            prev = cur
            cur = cur.next
        return r