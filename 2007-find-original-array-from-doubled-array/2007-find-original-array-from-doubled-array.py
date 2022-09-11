class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        arr = [0] * (10 ** 5 + 1)
        for n in changed:
            arr[n] += 1
        ans = []
        if arr[0] % 2 != 0: return []
        for _ in range(arr[0] // 2):
            ans.append(0)
        for i in reversed(range(1, len(arr))):
            if i % 2 != 0 or arr[i] == 0: continue
            for _ in range(arr[i]):
                ans.append(i // 2)
            arr[i // 2] -= arr[i]
            arr[i] = 0
        for i in range(1, len(arr)):
            if arr[i] != 0: return []
        return ans