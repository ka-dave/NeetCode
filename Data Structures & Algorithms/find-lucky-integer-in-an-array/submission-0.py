class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        res = 0
        hash_map = {}
        for i in arr:
            hash_map[i] = hash_map.get(i, 0) + 1
        
        for k in hash_map:
            if hash_map[k] == k:
                res = max(res, k)
        
        if res == 0:
            return -1
        return res
