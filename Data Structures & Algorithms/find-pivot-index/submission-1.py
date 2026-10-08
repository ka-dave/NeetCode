class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        

        prefix = []
        total = 0
        for i in nums:
            total += i
            prefix.append(total)

        #[1, 8, 11, 17, 22, 28]
        for i in range(len(nums)):
            if i-1 == -1:
                if 0 == prefix[-1] - prefix[i]:
                    return 0
            elif prefix[i-1] == prefix[-1] - prefix[i]:
                    return i
        return -1