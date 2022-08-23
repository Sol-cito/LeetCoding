# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def search(front, back, res):
            if not back:return front
            f = search(front, back.next, res)
            if f.val != back.val: res[0] = False
            return f.next
                
        res = [True]
        search(head, head, res)
        return res[0]
            
            
        
        
        