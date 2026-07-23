class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        h = {}
        for i in range(len(numbers)):
            h[numbers[i]] = i
        
        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in h and h[diff] != i:
                return [i+1,h[diff]+1]
        