class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(cur, prev, cnt, k):
            if not cur: return -1
            if cnt == k:
                temp = cur.next
                cur.next = prev
                return [cur, temp]
            res = reverse(cur.next, cur, cnt + 1, k)
            if res != -1: cur.next = prev
            return res

        cur = head
        prev = None
        nodeCnt = 0
        while cur:
            if nodeCnt % k == 0:
                res = reverse(cur, prev, 1, k)
                if res == -1: break
                if prev: prev.next = res[0]
                cur.next = res[1]
                cur = res[0]
                if nodeCnt == 0: head = cur
            prev = cur
            cur = cur.next
            nodeCnt += 1
        return head