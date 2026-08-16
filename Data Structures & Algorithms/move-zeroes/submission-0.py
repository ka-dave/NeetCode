class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i <= len(nums)-1:
            if nums[i] == 0:
                popped = nums.pop(nums.index(nums[i]))
                nums.append(popped)
            i += 1

        return nums