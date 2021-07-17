class Solution(object):
    def sweep(self, arr, candy):
        for i in range(0, len(arr) - 1):
            if arr[i] < arr[i + 1]: candy[i + 1] = max(candy[i + 1], candy[i] + 1)
        return candy

    def candy(self, ratings):
        candy = [1] * len(ratings)
        self.sweep(ratings, candy)
        res = self.sweep(ratings[::-1], candy[::-1])
        return sum(res)
