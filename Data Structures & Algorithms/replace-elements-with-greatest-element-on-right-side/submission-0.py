class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        res = []
        for i in range(len(arr)-1):
            m = 0
            for j in range(i+1, len(arr)):
                if arr[j] > m:
                    m = arr[j]
            res.append(m)
        res.append(-1)
        return res
