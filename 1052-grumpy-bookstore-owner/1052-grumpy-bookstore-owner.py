class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = sum(customers[:minutes])
        for i in range(minutes, len(grumpy)):
            if grumpy[i] == 0: total += customers[i]
        ans = total
        for i in range(minutes, len(grumpy)):
            total += customers[i] if grumpy[i] == 1 else 0
            total -= customers[i - minutes] if grumpy[i - minutes] == 1 else 0
            ans = max(ans, total)
        return ans