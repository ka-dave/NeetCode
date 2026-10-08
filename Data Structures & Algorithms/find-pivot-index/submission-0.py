class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = []
        for i in range(1, len(nums)+1):
            prefix.append(sum(nums[:i]))

        # [1, 8, 11, 17, 22, 28]
        for i in range(len(nums)):
            if i-1 == -1:
                if 0 == prefix[-1] - prefix[i]:
                    return 0
            elif prefix[i-1] == prefix[-1] - prefix[i]:
                    return i
        return -1