class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        leftBalls, leftDistTotal, rightBalls, rightDistTotal = 0, 0, 0, 0
        for i in reversed(range(1, len(boxes))):
            if boxes[i] == '1':
                rightBalls += 1
                rightDistTotal += i
        for i in range(len(boxes)):
            ans.append(leftDistTotal + rightDistTotal)
            rightDistTotal -= rightBalls
            if i < len(boxes) - 1 and boxes[i + 1] == '1':
                rightBalls -= 1
            if boxes[i] == '1':
                leftBalls += 1
            leftDistTotal += leftBalls
        return ans
