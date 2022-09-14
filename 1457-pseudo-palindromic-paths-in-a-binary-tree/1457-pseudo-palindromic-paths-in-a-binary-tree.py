class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, arr):
            if not cur.left and not cur.right:
                return 1 if len(list(filter(lambda x: x % 2 != 0, arr))) <= 1 else 0
            res = 0
            if cur.left:
                arr[cur.left.val - 1] += 1
                res += dfs(cur.left, arr)
                arr[cur.left.val - 1] -= 1
            if cur.right:
                arr[cur.right.val - 1] += 1
                res += dfs(cur.right, arr)
                arr[cur.right.val - 1] -= 1
            return res

        arr = [0] * 9
        arr[root.val - 1] += 1
        return dfs(root, arr)