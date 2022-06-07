class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        leftBalls, leftDist, rightBalls, rightDist = 0, 0, 0, 0
        for i in reversed(range(1, len(boxes))):
            if boxes[i] == '1':
                rightBalls += 1
                rightDist += i
        for i in range(len(boxes)):
            ans.append(leftDist + rightDist)
            rightDist -= rightBalls
            if boxes[i] == '1':
                leftBalls += 1
            if i < len(boxes) - 1 and boxes[i + 1] == '1':
                rightBalls -= 1
            leftDist += leftBalls
        return ans