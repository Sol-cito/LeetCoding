class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while cur:
            if cur.val == -10**7:return True
            cur.val = -10**7
            cur = cur.next
        return False