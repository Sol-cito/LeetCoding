class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total = 0
        cur = head
        while cur:
            total += 1
            cur = cur.next
        cur, prev = head, head
        cnt = 0
        ans = [None] * k
        idx = 0
        while cur:
            cnt += 1
            if cnt == math.ceil(total / k):
                ans[idx] = prev
                prev = cur
                total -= cnt
                k -= 1
                idx += 1
                cnt = 0
            cur = cur.next
            if cnt == 0:
                prev.next = None
                prev = cur
        return ans