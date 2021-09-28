class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, dic):
            if not node: return 0
            sum = node.val + dfs(node.left, dic) + dfs(node.right, dic)
            if sum not in dic.keys():
                dic[sum] = 1
            else:
                dic[sum] = dic.get(sum) + 1
            return sum

        dic = {}
        dfs(root, dic)
        heap = []
        for ele in dic.keys():
            heapq.heappush(heap, (-dic.get(ele), ele))
        firstPop = heapq.heappop(heap)
        ans = [firstPop[1]]
        num = -firstPop[0]
        while heap:
            pop = heapq.heappop(heap)
            if -pop[0] < num:break
            ans.append(pop[1])
        return ans