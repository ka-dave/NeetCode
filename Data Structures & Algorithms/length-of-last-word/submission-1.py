class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        split_s = s.split(" ")
        return len(split_s[-1])