class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = 0
        if bottom < special[0]: ans = special[0] - bottom
        if top > special[-1]: ans = max(ans, top - special[-1])
        for i in range(len(special) - 1):
            if special[i + 1] - special[i] > 1:
                ans = max(ans, special[i + 1] - special[i] - 1)
        return ans