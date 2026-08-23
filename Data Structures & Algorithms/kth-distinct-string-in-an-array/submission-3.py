class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        freq = defaultdict(int)

        for item in arr:
            freq[item] += 1

        for key,val in freq.items():
            if val == 1:
                res.append(key)
        
        if len(res) < k:
            return ""

        return res[k-1]