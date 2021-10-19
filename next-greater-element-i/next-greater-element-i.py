class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums2)):
            dic[nums2[i]] = i
        ans = []
        for ele in nums1:
            isFound = False
            for i in range(dic.get(ele) + 1, len(nums2)):
                if nums2[i] > ele:
                    ans.append(nums2[i])
                    isFound = True
                    break
            if not isFound:ans.append(-1)
        return ans