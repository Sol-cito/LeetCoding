class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [0] * len(prices)
        ans = 0
        minValue = prices[0]
        for i in range(1, len(prices)):
            arr[i] = max(arr[i - 1], prices[i] - minValue)
            minValue = min(minValue, prices[i])
            ans = max(ans, arr[i])
        nPrices = prices.copy()
        for i in range(1, len(prices)):
            nPrices[i] -= arr[i - 1]
        minValue = nPrices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - minValue)
            minValue = min(minValue, nPrices[i])
        return ans
