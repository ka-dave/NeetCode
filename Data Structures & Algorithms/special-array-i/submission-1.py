class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        for i in range(len(nums)-1):
            s = nums[i] + nums[i+1]

            if s % 2 == 0:
                return False
        return True
