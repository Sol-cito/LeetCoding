class Solution:
    origin = []
    nums = []
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.origin = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.origin.copy()
        return self.nums
        

    def shuffle(self) -> List[int]:
        shuffled = []
        while self.nums:
            idx = random.randrange(1, 100) % len(self.nums)
            shuffled.append(self.nums[idx])
            del self.nums[idx]
        self.nums = shuffled.copy()
        return shuffled