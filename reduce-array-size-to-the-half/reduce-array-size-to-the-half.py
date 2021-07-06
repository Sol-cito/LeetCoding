class Solution(object):
    def minSetSize(self, arr):
        numArr = [0] * 10 ** 5
        for ele in arr:
            numArr[ele - 1] += 1
        ansArr = []
        for n in numArr:
            if n > 0: ansArr.append(n)
        ansArr.sort(reverse=True)
        sum = 0
        for i in range(len(ansArr)):
            sum += ansArr[i]
            if sum >= len(arr) / 2: 
                return i + 1