class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len = float('inf')
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)

        i = 0
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        return word[:i]