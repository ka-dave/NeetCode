class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hashmap_s = {}
        hashmap_t = {}
        ss = ''
        tt = ''
        num_s = 0
        num_t = 0

        for i in s:
            if i not in hashmap_s:
                hashmap_s[i] = num_s
                num_s += 1
            ss += str(hashmap_s[i])

        for i in t:
            if i not in hashmap_t:
                hashmap_t[i] = num_t
                num_t += 1
            tt += str(hashmap_t[i])

        if ss == tt:
            return True
        return False