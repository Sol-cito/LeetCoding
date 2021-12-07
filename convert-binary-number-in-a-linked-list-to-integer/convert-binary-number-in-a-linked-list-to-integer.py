class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def search(node, cnt, res):
            if not node:return 0
            res[0] +=1
            search(node.next, cnt + 1, res)
            res[1] += node.val * 2 ** (res[0] - cnt)
            
        res = [0, 0]
        search(head, 1, res)
        return res[1]