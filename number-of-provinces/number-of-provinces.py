class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(node, parents):
            if node == parents[node]: return node
            res = find(parents[node], parents)
            parents[node] = res
            return res

        def union(n1, n2, parents):
            r1 = find(n1, parents)
            r2 = find(n2, parents)
            if r1 < r2:
                parents[r2] = r1
            else:
                parents[r1] = r2

        parents = [i for i in range(len(isConnected))]
        S = set([])
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    union(i, j, parents)
        for ele in parents:
            S.add(find(ele, parents))
        return len(S)