class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        m = {}

        for i in ransomNote:
            r[i] = r.get(i, 0) + 1

        for i in magazine:
            m[i] = m.get(i, 0) + 1

        for k,v in r.items():
            if m.get(k, 0) < v:
                return False 

        return True  
