class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = dict(zip([ele for ele in nums1], [0 for _ in range(len(nums1))]))
        for ele in nums1:
            dic[ele] +=1
        ans = []
        for ele in nums2:
            if ele in dic and dic[ele] > 0:
                dic[ele] = dic.get(ele) - 1
                ans.append(ele)
        return ans