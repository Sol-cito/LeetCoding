class Solution(object):
    def findAncestorOfNode1(self, node, dic, S):
        S.add(node)
        if not dic.get(node): return S
        return self.findAncestorOfNode1(dic.get(node), dic, S)
    
    def findAncestorOfNode2(self, node, dic, S):
        if node in S: return node
        return self.findAncestorOfNode2(dic.get(node), dic, S)

    def storeParent(self, node, dic):
        if node.left:
            dic[node.left] = node
            self.storeParent(node.left, dic)
        if node.right:
            dic[node.right] = node
            self.storeParent(node.right, dic)

    def lowestCommonAncestor(self, root, p, q):
        dic = {}
        self.storeParent(root, dic)
        S = self.findAncestorOfNode1(p, dic, set([]))
        return self.findAncestorOfNode2(q, dic, S)
