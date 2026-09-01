class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        h = {}
        res = []
        
        for i in nums:
            h[i] = h.get(i,0) + 1
        
        val = 0
        for k,v in h.items():
            if val < v:
                val = v
                res = k
        return res