class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def search(front, back):
            if not back:return front
            f = search(front, back.next)
            if f == -1:return -1
            if f.val != back.val: return -1
            return f.next
                
        return False if search(head, head) == -1 else True
            
            
        
        
        