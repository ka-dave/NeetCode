class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
                nums.insert(i, float('-inf'))
                nums.pop(i+1)
        
        nums.sort(reverse=True)
        return int(len(nums)) - int(count)