# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dic = dict()
        dic[0] = ListNode(-1, head)
        idx = 1
        cur = head
        while cur:
            dic[idx] = cur
            idx += 1
            cur = cur.next
        dic[idx] = None
        if abs(k - (idx - k)) <= 1:
            a, b = min(k, idx - k), max(k, idx - k)
            dic.get(a - 1).next = dic.get(b)
            dic.get(b).next = dic.get(a)
            dic.get(a).next = dic.get(b + 1)
        else:
            dic.get(k - 1).next = dic.get(idx - k)
            dic.get(idx - k - 1).next = dic.get(k)
            dic.get(idx - k).next = dic.get(k + 1)
            dic.get(k).next = dic.get(idx - k + 1)
        return dic.get(0).next