class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            res = 0
            for j in range(len(boxes)):
                if i == j:continue
                if boxes[j] == '1':
                   res += abs(i - j)
            ans.append(res)
        return ans