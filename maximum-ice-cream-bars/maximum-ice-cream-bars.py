class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        remain, ans = coins, 0
        for ele in costs:
            if remain < ele: break
            remain -= ele
            ans +=1
        return ans