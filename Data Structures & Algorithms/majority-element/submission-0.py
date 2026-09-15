class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        s_nums = set(nums)

        for i in s_nums:
            if nums.count(i) > len(nums) / 2:
                return i