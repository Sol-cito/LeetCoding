class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def search(node, arr):
            if not node:return 0
            a,b = search(node.left, arr), search(node.right, arr)
            arr[0] += abs(a - b)
            return a + b + node.val
        
        arr = [0]
        search(root, arr)
        return arr[0]