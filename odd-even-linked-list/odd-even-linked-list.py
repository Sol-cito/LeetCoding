class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        numOfNodes, lastNode = 1, head
        while lastNode.next:
            lastNode = lastNode.next
            numOfNodes += 1
        if numOfNodes <= 2: return head
        cnt, pre, cur = 0, head, head.next
        while cnt < numOfNodes // 2:
            pre.next = cur.next
            pre = cur.next
            lastNode.next = cur
            lastNode = cur
            lastNode.next = None
            cur = pre.next
            cnt += 1
        return head