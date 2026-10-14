class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        counter = 0
        res = []
        counts = []

        for i in s:
            if i in res:
                counter = 0
                res = res[res.index(i)+1:]
                counter = len(res)
            
            res.append(i)
            counter += 1
            counts.append(counter)

        counts.sort()
        return counts[-1]