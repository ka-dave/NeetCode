class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s= s.strip()
        s_s = s.split(" ")

        return len(s_s[-1])