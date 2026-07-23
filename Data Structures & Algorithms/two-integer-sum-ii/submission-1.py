class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numbers:
                j = numbers.index(diff)
                numbers.pop(j)
                if i < j:
                    return [i+1,j+1]