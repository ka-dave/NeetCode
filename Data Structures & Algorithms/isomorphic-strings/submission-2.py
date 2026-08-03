class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashmap_s = {}
        hashmap_t = {}
        ss = 0
        tt = 0
        result_s = ''
        result_t = ''

        for i in s:
            if i not in hashmap_s:
                hashmap_s[i] = ss
                ss += 1 
            result_s += str(hashmap_s[i])
        
        for i in t:
            if i not in hashmap_t:
                hashmap_t[i] = tt
                tt += 1
            result_t += str(hashmap_t[i])

        if result_s == result_t:
            return True
        return False