class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if len(tokens) == 0 or power < tokens[0]:return 0
        l, r = 0, len(tokens) - 1
        ans = 0
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                l += 1
                ans += 1
            else:
                if l != r:
                    power += tokens[r]
                    ans -= 1
                r -= 1
        return ans