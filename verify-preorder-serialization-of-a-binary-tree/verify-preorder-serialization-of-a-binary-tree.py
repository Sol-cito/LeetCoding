class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        def recursion(preorder, pointer):
            if pointer >= len(preorder): return -1
            if preorder[pointer] == '#': return pointer
            res1 = recursion(preorder, pointer + 1)
            if res1 == -1: return -1
            res2 = recursion(preorder, res1 + 1)
            return res2

        preorder = preorder.split(",")
        res = recursion(preorder, 0)
        return res != -1 and res == len(preorder) - 1