class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if len(pattern) != len(list(s.split(" "))):
            return False

        if len(set(pattern)) == len(set(list(s.split(" ")))):
            return True
        else:
            return False