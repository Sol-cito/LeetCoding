class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def getRegionInfo(visit, i, j):
            nextInfectedVisit = [[False] * len(isInfected[0]) for _ in range(len(isInfected))]
            visit[i][j] = True
            que = deque([[i, j]])
            numOfWalls = 0
            numOfNextInfected = 0
            region = []
            while que:
                pop = que.pop()
                region.append(pop)
                for dx, dy in DIR:
                    nx, ny = pop[0] + dx, pop[1] + dy
                    if 0 <= nx < len(isInfected) and 0 <= ny < len(isInfected[0]) and isInfected[nx][
                        ny] == 0: numOfWalls += 1
                    if 0 <= nx < len(isInfected) and 0 <= ny < len(isInfected[0]) and isInfected[nx][
                        ny] == 0 and not nextInfectedVisit[nx][ny]:
                        nextInfectedVisit[nx][ny] = True
                        numOfNextInfected += 1
                    if 0 <= nx < len(isInfected) and 0 <= ny < len(isInfected[0]) and isInfected[nx][
                        ny] == 1 and not visit[nx][ny]:
                        visit[nx][ny] = True
                        que.appendleft([nx, ny])
            return numOfWalls, numOfNextInfected, region

        def paintRegion(region):
            for x, y in region:
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(isInfected) and 0 <= ny < len(isInfected[0]) and isInfected[nx][ny] == 0:isInfected[nx][ny] = 1

        def quarantineRegion(region):
            for x, y in region:
                isInfected[x][y] = 'x'

        ans = 0
        while True:
            nextNumOfWalls = 0
            maxNumOfNextInfected = 0
            regionInfos = []
            visit = [[False] * len(isInfected[0]) for _ in range(len(isInfected))]
            for i in range(len(isInfected)):
                for j in range(len(isInfected[0])):
                    if isInfected[i][j] == 1 and not visit[i][j]:
                        numOfWalls, numOfNextInfected, region = getRegionInfo(visit, i, j)
                        if numOfNextInfected > maxNumOfNextInfected:
                            maxNumOfNextInfected = numOfNextInfected
                            nextNumOfWalls = numOfWalls
                        regionInfos.append([numOfNextInfected, region])
            if maxNumOfNextInfected == 0: break
            ans += nextNumOfWalls
            for ni, r in regionInfos:
                if ni == maxNumOfNextInfected:
                    quarantineRegion(r)
                else:
                    paintRegion(r)
        return ans