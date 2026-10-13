class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        res = 0
        hash_map = {}
        for i in arr:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        
        for k in hash_map:
            if hash_map[k] == k:
                res = max(res, k)
        
        if res == 0:
            return -1
        return res
