class MinStack:
    def __init__(self):
        self.minValue = 0
        self.stack = []
        self.pointer = 0

    def push(self, val: int) -> None:
        if len(self.stack) == self.pointer:
            self.stack.append(0)
        self.stack[self.pointer] = val
        self.pointer += 1

    def pop(self) -> None:
        self.pointer -= 1

    def top(self) -> int:
        return self.stack[self.pointer - 1]

    def getMin(self) -> int:
        return min(self.stack[:self.pointer])