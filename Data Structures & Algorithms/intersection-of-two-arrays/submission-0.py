class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1_s = set(nums1)
        nums2_s = set(nums2)
        result = []

        for i in nums1_s:
            if i in nums2_s:
                result.append(i)
        return result