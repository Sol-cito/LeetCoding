class FreqStack:
    def __init__(self):
        self.heap = []
        self.dic = {}
        self.dist = 0

    def push(self, val: int) -> None:
        if val in self.dic:
            self.dic[val] = self.dic.get(val) - 1
        else:
            self.dic[val] = -1
        heapq.heappush(self.heap, [self.dic.get(val), self.dist, val])
        self.dist -= 1

    def pop(self) -> int:
        pop = heapq.heappop(self.heap)
        self.dic[pop[2]] = self.dic.get(pop[2]) + 1
        return pop[2]