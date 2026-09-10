class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = ''
        for i in digits:
            s += str(i)
        
        final = int(s) + 1
        return list(str(final))