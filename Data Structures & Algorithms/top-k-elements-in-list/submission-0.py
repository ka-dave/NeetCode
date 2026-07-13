class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h = {}
        result = []

        for i in nums:
            h[i] = nums.count(i)

        sorted_h = sorted(h.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            result.append(sorted_h[i][0])
        
        return result