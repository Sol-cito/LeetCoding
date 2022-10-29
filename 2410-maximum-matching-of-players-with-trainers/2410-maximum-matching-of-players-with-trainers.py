class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pointer = 0
        ans = 0
        for p in players:
            while pointer < len(trainers):
                if trainers[pointer] >= p:
                    pointer += 1
                    ans += 1
                    break
                pointer += 1
        return ans