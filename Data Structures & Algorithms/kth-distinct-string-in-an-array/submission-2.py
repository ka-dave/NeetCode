class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []

        for key,val in Counter(arr).items():
            if val == 1:
                res.append(key)
        
        if len(res) < k:
            return ""

        return res[k-1]