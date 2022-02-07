class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        def merge(root, x, y):
            xRoot, yRoot = find(root, x), find(root, y)
            if xRoot <= yRoot:
                root[yRoot] = xRoot
            else:
                root[xRoot] = yRoot

        def find(root, num):
            if root[num] == num: return num
            res = find(root, root[num])
            root[num] = res
            return res

        ans = []
        root = [i for i in range(n)]
        for req1, req2 in requests:
            req1_root, req2_root = find(root, req1), find(root, req2)
            canBeFriends = True
            for rest1, rest2 in restrictions:
                rest1_root, rest2_root = find(root, rest1), find(root, rest2)
                if (req1_root == rest1_root and req2_root == rest2_root) or (
                        req2_root == rest1_root and req1_root == rest2_root):
                    canBeFriends = False
                    break
            if canBeFriends:
                ans.append(True)
                merge(root, req1, req2)
            else:
                ans.append(False)
        return ans