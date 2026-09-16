class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
 
        if len(nums) == 1:
            return True

        if nums[0] % 2 == 0:
            check = True
        else:
            check = False

        for i in range(1,len(nums)):
            if check == True:
                if nums[i] % 2 == 0:
                    return False
                else:
                    check = False
            elif check == False:
                if nums[i] % 2 != 0:
                    return False
                else:
                    check = True
        
        return True