class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res, target, cur, val = None, head, head, 0
        while cur:
            if cur.val == 0 and val > 0:
                n = ListNode(val)
                if not res:res = n
                target.next = n
                target = n
                val = 0
            val += cur.val
            cur = cur.next
        return res