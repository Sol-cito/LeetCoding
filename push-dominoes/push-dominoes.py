class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        arr = list(dominoes)
        que_l, que_r = deque([]), deque([])
        for i in range(len(arr)):
            if arr[i] == 'L':
                que_l.appendleft(i)
            elif arr[i] == 'R':
                que_r.appendleft(i)
        while que_l or que_r:
            nQue_l, nQue_r = deque([]), deque([])
            S = set([])
            while que_l:
                pop = que_l.pop()
                if pop > 0 and arr[pop - 1] == '.':
                    if pop > 1 and arr[pop - 1] == '.' and arr[pop - 2] == 'R': continue
                    arr[pop - 1] = 'L'
                    nQue_l.appendleft(pop - 1)
                    S.add(pop - 1)
            while que_r:
                pop = que_r.pop()
                if pop < len(arr) - 1 and arr[pop + 1] == '.':
                    if pop < len(arr) - 2 and arr[pop + 1] == '.' and arr[pop + 2] == 'L' and (
                            pop + 2) not in S: continue
                    arr[pop + 1] = 'R'
                    nQue_r.appendleft(pop + 1)
            que_l = nQue_l
            que_r = nQue_r
        return "".join(arr)