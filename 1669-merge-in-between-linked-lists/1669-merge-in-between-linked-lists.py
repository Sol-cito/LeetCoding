class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev, end = None, None
        cur = list1
        cnt = 0
        while cur:
            if cnt == a - 1:prev = cur
            if cnt == b + 1:end = cur
            cur = cur.next
            cnt +=1
        cur = list2
        prev.next = list2
        while cur:
            if not cur.next:
                cur.next = end
                break
            cur = cur.next
        return list1