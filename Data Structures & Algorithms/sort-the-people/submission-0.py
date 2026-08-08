class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        h = zip(names,heights)
        s = sorted(list(h), key=lambda x: (x[1], x[0]), reverse=True)

        res = []
        for i in s:
            res.append(i[0])
        
        return res