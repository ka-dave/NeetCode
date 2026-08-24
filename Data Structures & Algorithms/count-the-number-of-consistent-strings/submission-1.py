class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = []
        allowed_l = list(allowed)

        for word in words:
            count = 0
            for i in word:
                if i in allowed:
                    count += 1
            
            if count == len(word):
                res.append(word)
        
        return len(res)