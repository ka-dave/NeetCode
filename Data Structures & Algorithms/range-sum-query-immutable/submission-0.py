class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        
        total = 0
        prefix = []
        for i in range(len(self.nums)):
            total += self.nums[i]
            prefix.append(total)

        result = 0
        for i in range(left, right+1):
            result += self.nums[i]
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)