class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        preSum = 0
        for i in range(k):
            preSum += cardPoints[i]
        ans = preSum
        rare = len(cardPoints) - 1
        front = k - 1
        for _ in range(k):
            preSum = preSum - cardPoints[front] + cardPoints[rare]
            ans = max(ans, preSum)
            front -= 1
            rare -= 1
        return ans