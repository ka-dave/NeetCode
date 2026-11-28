class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1_s = set(nums1)
        result = []

        for i in nums2:
            if i in nums1_s:
                result.append(i)
                nums1_s.remove(i)
        return result