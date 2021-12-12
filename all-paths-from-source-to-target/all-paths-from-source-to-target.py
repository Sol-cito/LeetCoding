class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, dic, dir, ans):
            if cur == len(dic) - 1:
                ans.append(dir.copy())
                return
            for linked in dic.get(cur):
                dir.append(linked)
                dfs(linked, dic, dir, ans)
                del dir[-1]
            return
            
            
        ans = []
        dic = {}
        for i in range(len(graph)):
            dic[i] = graph[i]
        dfs(0, dic, [0], ans)
        return ans            
            
            