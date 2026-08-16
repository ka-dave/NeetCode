class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        indexs = []

        for i in nums1:
            indexs.append(nums2.index(i))

        for i in range(len(nums1)):
            exist = False
            for j in range(indexs[i]+1,len(nums2)):
                if nums2[j] > nums1[i]:
                    exist = True
                    res.append(nums2[j])
                    break

            if exist == False:
                res.append(-1)

        return res