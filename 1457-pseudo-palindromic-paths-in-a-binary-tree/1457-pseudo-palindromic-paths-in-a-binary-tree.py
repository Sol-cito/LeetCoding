class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, arr):
            if not cur: return 0
            arr[cur.val - 1] += 1
            res = 0
            if not cur.left and not cur.right:
                if len(list(filter(lambda x: x % 2 != 0, arr))) <= 1: res += 1
            res += dfs(cur.left, arr.copy())
            res += dfs(cur.right, arr.copy())
            return res

        arr = [0] * 9
        return dfs(root, arr)