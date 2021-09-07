class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        answer = [releaseTimes[0], keysPressed[0]]
        for i in range(1, len(releaseTimes)):
            a, b = releaseTimes[i] - releaseTimes[i - 1], keysPressed[i]
            if answer[0] < a or answer[0] == a and ord(answer[1]) < ord(b):
                answer = [a, b]
        return answer[1]