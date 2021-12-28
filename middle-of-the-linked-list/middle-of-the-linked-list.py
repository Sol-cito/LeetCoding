# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        dic = {}
        cur = head
        while cur:
            dic[cnt] = cur
            cur = cur.next
            cnt +=1
        return dic[cnt//2]
        