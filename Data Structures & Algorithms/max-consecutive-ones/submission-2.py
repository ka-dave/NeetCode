class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        count = 0

        for i in nums:
            if i == 1:
                count += 1
                res.append(count)
            else:
                count = 0

        res.sort(reverse=True)
        if res:
            return res[0]
        else: 
            return 0