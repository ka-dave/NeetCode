class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        freq = {}

        for item in arr:
            freq[item] = freq.get(item, 0) + 1

        for key,val in freq.items():
            if val == 1:
                res.append(key)
        
        if len(res) < k:
            return ""

        return res[k-1]